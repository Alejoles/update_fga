import requests
from datetime import datetime
from helpers import (read_csv_pandas, filter_data)
from webservice import (lineru_get_applications, fga_get_bearer_token, fga_update_balance_webservice)



if __name__ == "__main__":
    failed_lineru_list = []
    failed_fga_update_list = []
    df = read_csv_pandas()
    df_filtered = filter_data(df)
    # bearer_token = fga_get_bearer_token()
    for index, row in df_filtered.iterrows():
        pagare = row["Agosto"]
        fecha_corte = row["fecha-corte"]
        """
            body_lineru, failed_lineru_webservice = lineru_get_applications(pagare, fecha_corte)
            if failed_lineru_webservice != "":
                failed_lineru_list.append(failed_lineru_webservice)
            failed_fga_webservice = fga_update_balance_webservice(body_lineru, bearer_token)
            if failed_fga_webservice != "":
                failed_fga_update_list.append(failed_fga_webservice)
        """
