import requests
from datetime import datetime
import json
from constants import (
    LINERU_SERVICE_URL,
    LINERU_SERVICE_KEY,
    NIT,
    FGA_API_KEY_URL,
    PASSWORD_API_KEY_FGA,
    USERNAME_API_KEY_FGA,
    FGA_UPDATE_BALANCE_URL
)
from helpers import calculate_default

def lineru_get_applications(credit_reference: str, cutoff_date: str, value_from_csv: int):
    failed_lineru_reference = ""
    url = f"{LINERU_SERVICE_URL}/api/applications/{credit_reference}/calculator?date={cutoff_date}&status=1"
    headers = {"X-Api-Key": LINERU_SERVICE_KEY,
               "Content-Type": "application/json"
    }
    resp = requests.get(url, headers=headers)
    # Check the response status code
    response = resp.json()
    if resp.status_code != 200:
        # Request was unsuccessful
        print(f"Request failed with status code: {resp.status_code}, reference:{credit_reference}")
        failed_lineru_reference = credit_reference

    balance_update_obj = {
        'nit': NIT,
        'cedula': str(response["document"]),
        'pagare': credit_reference,
        'valor_comision_reportado': value_from_csv,
        'saldo_capital': int(response["principal"]),
        'saldo_total': int(response["balance"]),
        'fecha_corte': cutoff_date,
        'num_cuotas_mora': "",
        'fec_inicio_mora': "",
        'fecha_cancelacion': "", # En FGA se envia vacio al parecer
        'estado_operacion': "M",
    }

    if response["is_paid"]:
        balance_update_obj["estado_operacion"] = "C"
        balance_update_obj['fecha_cancelacion'] = str(response["closed_at"])
    else:
		# compare if date is greater or equal than today
        date1 = datetime.strptime(response["due_date"], "%Y-%m-%d")
        date2 = datetime.strptime(cutoff_date, "%Y-%m-%d")
        if date1 >= date2:
            balance_update_obj["estado_operacion"] = "V"
        else:
            balance_update_obj["num_cuotas_mora"] = calculate_default(str(response["due_date"]), cutoff_date),
            balance_update_obj["fec_inicio_mora"] = str(response["due_date"])
            balance_update_obj["estado_operacion"] = "M"

    return balance_update_obj, failed_lineru_reference


def lineru_get_applications_without_values(credit_reference: str, cutoff_date: str):
    failed_lineru_reference = ""
    cutoff_date_modified = cutoff_date.split("-")[:2]
    cutoff_date_modified_final = cutoff_date_modified[0] + "-" + cutoff_date_modified[1]
    url = f"{LINERU_SERVICE_URL}/api/applications/{credit_reference}/calculator?date={cutoff_date}&status=1"
    headers = {"X-Api-Key": LINERU_SERVICE_KEY,
               "Content-Type": "application/json"
    }
    resp = requests.get(url, headers=headers)
    # Check the response status code
    response = resp.json()
    if resp.status_code != 200:
        # Request was unsuccessful
        print(f"Request failed with status code: {resp.status_code}, reference:{credit_reference}")
        failed_lineru_reference = credit_reference
    print("Response:    ", response["fga_by_month"])
    if response["fga_by_month"] != []:
        if cutoff_date_modified_final in response["fga_by_month"].keys():
            object_to_return = {
                'pagare': credit_reference,
                'fecha_corte': cutoff_date,
                'valor_comision_reportado': str(response["fga_by_month"][cutoff_date_modified_final]),
            }
            print("YES")
        else:
            object_to_return = {
            'pagare': credit_reference,
            'fecha_corte': cutoff_date,
            'valor_comision_reportado': "",
        }
    else:
        object_to_return = {
            'pagare': credit_reference,
            'fecha_corte': cutoff_date,
            'valor_comision_reportado': "",
        }

    return object_to_return, failed_lineru_reference



def fga_get_bearer_token():
    url = FGA_API_KEY_URL
    headers = {
        "Content-Type": "application/json"
    }
    body_dict = {
        "username": USERNAME_API_KEY_FGA,
        "password": PASSWORD_API_KEY_FGA
    }
    response = requests.post(url, headers=headers, json=body_dict)
    if response.status_code != 200:
        print("Failed to get bearer token from FGA, error:", response.json())
        raise Exception
    return response.json()["access_token"]


def fga_update_balance_webservice(body_from_lineru_webservice, bearer_token):
    failed_fga_update = ""
    url = FGA_UPDATE_BALANCE_URL
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=body_from_lineru_webservice)
    response_json = response.json()
    if response.status_code != 200 and response.status_code != 422:
        failed_fga_update = response.json()
        print("Failed in updating fga: ", response_json)
    elif response.status_code == 401:
        print("Unauthenticated")
    elif response.status_code != 200:
        print("Only different from 200: ", response_json)
    return response.json(), failed_fga_update
