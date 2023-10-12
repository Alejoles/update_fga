from helpers import create_csv_from_dict, read_csv_pandas_get_values, get_value_from_lineru_body
from webservice import lineru_get_applications_without_values


if __name__ == "__main__":
    money_left_to_process = 1048000
    procesing_money = 0
    failed_lineru_list = []
    success_lineru_list = []
    df = read_csv_pandas_get_values()
    count = 0
    for index, row in df.iterrows():
        failed_lineru_list = []
        success_lineru_list = []
        pagare = str(row["referencia_credito"])
        fecha_corte = "2023-09-30"
        print("Archivos procesados: ", count)
        body_lineru, failed_lineru_webservice = lineru_get_applications_without_values(pagare, fecha_corte)
        if body_lineru["valor_comision_reportado"] == "":
            continue
        procesing_money += get_value_from_lineru_body(body_lineru)
        print("Procesing Money: ", procesing_money)
        success_lineru_list.append(body_lineru)
        if failed_lineru_webservice != "":
            failed_lineru_list.append(failed_lineru_webservice)
            print("En lineru falló un archivo con código: ", pagare)
        count += 1
        create_csv_from_dict([body_lineru], "success_lineru_list.csv")
        create_csv_from_dict(failed_lineru_list, "failed_lineru_list.csv")
        if procesing_money >= money_left_to_process:
            print("stopped")
            break
    print(failed_lineru_list)
