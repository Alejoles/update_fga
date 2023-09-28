import requests
from datetime import datetime

import pandas as pd
from webservice import lineru_get_applications

# Function that reads the csv file and returns the data needed.
def read_csv_pandas():
    # Replace 'your_file.csv' with the path to your CSV file
    file_path = 'file.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Select the two columns you want to keep (replace 'column1' and 'column2' with the actual column names)
    selected_columns = df[['Agosto', 'fecha-corte']]
    return selected_columns



if __name__ == "__main__":
    lineru_get_applications(66852236, "2023-08-31")