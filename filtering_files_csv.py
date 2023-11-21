import pandas as pd


if __name__ == "__main__":
    df_new_apps = pd.read_csv("new_apps.csv")
    df_to_delete = pd.read_csv("success_lineru_list.csv")

    values_to_delete = df_to_delete["pagare"].tolist()

    df_filtered = df_new_apps[df_new_apps['referencia_credito'].isin(values_to_delete)]
    df_filtered.to_csv("data_review.csv", index=False)
    pass
