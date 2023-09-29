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
    response = requests.get(url, headers=headers)
    # Check the response status code
    if response.status_code != 200:
        # Request was unsuccessful
        print(f"Request failed with status code: {response.status_code}, reference:{credit_reference}")
        failed_lineru_reference = credit_reference

    balance_update_obj = {
        'nit': NIT,
        'cedula': str(response["document"]),
        'pagare': credit_reference,
        'valor_comision_reportado': value_from_csv,
        'saldo_capital': int(response["principal"]),
        'saldo_total': int(response["balance"]),
        'fecha_corte': cutoff_date,
        'num_cuotas_mora': calculate_default(str(response["due_date"]), cutoff_date),
        'fec_inicio_mora': str(response["due_date"]),
        'fecha_cancelacion': "", # En FGA se envia vacio al parecer
        'estado_operacion': "M",
    }

    return balance_update_obj, failed_lineru_reference



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
    if response.status_code != 200:
        failed_fga_update = response.json()
        return failed_fga_update
    return
