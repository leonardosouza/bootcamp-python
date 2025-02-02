import os
from glob import glob

import pandas as pd
from numpy import void


# consolidar json e extrair dados
def extract_data(folder_name: str) -> pd.DataFrame:
    type_files = "*.json"
    json_files = glob(os.path.join(folder_name, type_files))
    df_list = [pd.read_json(file) for file in json_files]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# transformar dados
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# carregar dados
def load_data(df: pd.DataFrame, export_format: list) -> void:
    for format in export_format:
        if format == "csv":
            df.to_csv("coleta_total.json", index=False)

        if format == "parquet":
            df.to_parquet("coleta_total.parquet", index=False)


def pipeline_calc_kpi(folder_name: str, export_type: list):
    data_frames = extract_data(folder_name)
    data_frames = transform_data(df=data_frames)
    load_data(df=data_frames, export_format=export_type)
