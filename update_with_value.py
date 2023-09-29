import requests
from datetime import datetime

import pandas as pd
from webservice import lineru_get_applications, fga_get_bearer_token, fga_update_balance_webservice

# Function that reads the csv file and returns the data needed.
def read_csv_pandas():
    # Replace 'your_file.csv' with the path to your CSV file
    file_path = 'file.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    print(df)
    # Select the two columns you want to keep (replace 'column1' and 'column2' with the actual column names)
    selected_columns = df[['Agosto', 'fecha-corte']]
    return selected_columns

def filter_data(df):
    # This function is to filter specific data, USE ONLY IF NEEDED
    df["Agosto"] = df["Agosto"].astype('float') * -1
    print(df)

if __name__ == "__main__":
    df = read_csv_pandas()
    print(filter_data(df))
    """
    body_lineru = lineru_get_applications(66852236, "2023-08-31")
    bearer_token = fga_get_bearer_token()
    fga_update_balance_webservice(body_lineru, bearer_token)

    """
    #lineru_get_applications(66852236, "2023-08-31")