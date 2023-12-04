from helpers import (read_csv_pandas_selected_columns, filter_data, create_csv)
from webservice import (lineru_get_applications, fga_get_bearer_token, fga_update_balance_webservice)



if __name__ == "__main__":
    print("Debug")
    failed_lineru_list = []
    failed_fga_update_list = []
    success_lineru_list = []
    success_fga_update_list = []
    df = read_csv_pandas_selected_columns()
    bearer_token = fga_get_bearer_token()
    count = 0
    for index, row in df.iterrows():
        pagare = str(row["referencia_credito"])
        valor_declarado = 1 #TODO: cambia
        fecha_corte = "2023-11-30" #TODO: cambia
        print("Archivos procesados: ", count)
        body_lineru, failed_lineru_webservice = lineru_get_applications(pagare, fecha_corte, valor_declarado)
        success_lineru_list.append(body_lineru)
        if failed_lineru_webservice != "":
            failed_lineru_list.append(failed_lineru_webservice)
            print("En lineru falló un archivo con código: ", pagare)

        body_fga, failed_fga_webservice = fga_update_balance_webservice(body_lineru, bearer_token)
        print(f"Respuesta fga: {body_fga}")
        success_fga_update_list.append(body_fga)
        if failed_fga_webservice != "":
            failed_fga_update_list.append(failed_fga_webservice)
            print("En fga falló un archivo con código: ", pagare)
        count += 1
    print(failed_lineru_list)
    print(failed_fga_update_list)
    create_csv(success_lineru_list, "success_lineru_csv.csv")
    create_csv(success_fga_update_list, "success_fga_update_csv.csv")
    create_csv(failed_lineru_list, "failed_lineru_csv.csv")
    create_csv(failed_fga_update_list, "failed_fga_update_csv.csv")
