import pandas as pd
from datetime import datetime

# Function that reads the csv file and returns the data needed.
def read_csv_pandas_selected_columns():
    # Replace 'your_file.csv' with the path to your CSV file
    file_path = 'data_review.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Select the three columns you want to keep
    selected_columns = df[['referencia_credito', 'datos_garantia.fecha_desembolso']]
    return selected_columns


def read_csv_pandas_get_values():
    # Replace 'your_file.csv' with the path to your CSV file
    file_path = 'new_apps.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Select the three columns you want to keep
    selected_columns = df[['referencia_credito']]
    return selected_columns

def filter_data(df):
    # This function is to filter specific data, USE ONLY IF NEEDED
    df["Agosto"] = df["Agosto"].astype('float') * -1
    return df


def calculate_default(due_date: str, cutoff: str):
    res = 0
    time_format = "%Y-%m-%d"  # Asumiendo un formato de fecha como "YYYY-MM-DD HH-MM-SS"

    due_date_time = datetime.strptime(due_date, time_format)
    cutoff_time = datetime.strptime(cutoff, time_format)

    while due_date_time < cutoff_time:
        due_date_time = due_date_time.replace(month=due_date_time.month + 1)
        res += 1

    if res > 2:
        return str(res - 1)
    else:
        return str(1)



def create_csv(list_of_values, filename: str):
    df = pd.DataFrame({'Values': list_of_values})
    df.to_csv(filename, index=False, header=False, sep=' ')

def create_csv_from_dict(dict_of_values, filename: str):
    df = pd.DataFrame(dict_of_values)
    df.to_csv(filename, mode='a', header=False, index=False)

def get_value_from_lineru_body(data: dict):
    return int(data["valor_comision_reportado"])