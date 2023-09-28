import requests
from datetime import datetime
from constants import (
    LINERU_SERVICE_URL,
    LINERU_SERVICE_KEY,
    NIT
)

def lineru_get_applications(credit_reference: str, cutoff_date: str):
    url = f"{LINERU_SERVICE_URL}/api/applications/{credit_reference}/calculator?date={cutoff_date}&status=1"
    headers = {"X-Api-Key": LINERU_SERVICE_KEY,
               "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    # Check the response status code
    if response.status_code != 200:
        # Request was unsuccessful
        print(f"Request failed with status code: {response.status_code}, reference:{credit_reference}")

    valor_comision_reportado = response.json()["fga_by_month"][cutoff_date[:7]]

    balance_update_obj = {
        'nit': NIT,
        'cedula': str(response["document"]),
        'pagare': credit_reference,
        'valor_comision_reportado': int(valor_comision_reportado),
        'saldo_capital': int(response["principal"]),
        'saldo_total': int(response["balance"]),
        'fecha_corte': cutoff_date,
        'num_cuotas_mora': "",
        'fec_inicio_mora': "",
        'fecha_cancelacion': "",
        'estado_operacion': "",
    }

    if response["is_paid"]:
        balance_update_obj['Request']['EstadoOperacion'] = "C"
        balance_update_obj['Request']['FechaCancelacion'] = str(response["closed_at"])
    else:
        # Compara si la fecha es mayor o igual a hoy
        date1 = datetime.strptime(response["due_date"], "%Y-%m-%d")
        date2 = datetime.strptime(cutoff_date, "%Y-%m-%d")
        if date1 >= date2:
            balance_update_obj['Request']['EstadoOperacion'] = "V"
        else:
            balance_update_obj['Request']['NumCuotasMora'] = CalculateDefault(str(response["due_date"]), cutoff) #TODO: realizar funcion para las cuotas
            balance_update_obj['Request']['FecInicioMora'] = str(response["due_date"])
            balance_update_obj['Request']['EstadoOperacion'] = "M"

    if response.get("zinobe_product_name") is not None:
        balance_update_obj['Request']['ZinobeProductName'] = str(response["zinobe_product_name"])

    return balance_update_obj


def fga_update_balance_webservice():
    url = f"{LINERU_SERVICE_URL}/api/applications/{credit_reference}/calculator?date={cutoff_date}&status=1"
    headers = {"X-Api-Key": LINERU_SERVICE_KEY,
               "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return
