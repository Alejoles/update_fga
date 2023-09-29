import pandas as pd
from datetime import datetime

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
    return df


def calculate_default(due_date: str, cutoff: str):
    res = 0
    time_format = "%Y-%m-%d"  # Asumiendo un formato de fecha como "YYYY-MM-DD"

    due_date_time = datetime.strptime(due_date, time_format)
    cutoff_time = datetime.strptime(cutoff, time_format)

    while due_date_time < cutoff_time:
        due_date_time = due_date_time.replace(year=due_date_time.year + 1)
        res += 1

    if res > 2:
        return str(res - 1)
    else:
        return str(1)