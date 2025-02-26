import os

import pandas as pd


class Importer:
    def __init__(self, file_name: str):
        self.file_path = f"{os.path.dirname(__file__)}/{file_name}"
        self.df = None
        self.filtered = None

    def load_from_csv(self):
        self.filtered = None
        self.df = pd.read_csv(self.file_path)
        return self

    def filter_by_collumn(self, column: str, value: any):
        if self.filtered is not None:
            self.filtered = self.filtered[self.filtered[column] == value]
        else:
            self.filtered = self.df[self.df[column] == value]
        return self

    def get_result(self):
        return self.filtered

    def get_all_data(self):
        return self.df
