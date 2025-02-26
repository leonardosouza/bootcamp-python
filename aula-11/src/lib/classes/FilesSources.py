import os

from AbstractDataSource import AbstractDataSource


class FilesSources(AbstractDataSource):
    def __init__(self):
        self.previous_files = []
        self.folder_path = None
        self.start()

    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files]

        if new_files:
            print("New files detected:", new_files)
            self.previous_files = current_files
        else:
            print("New files not detected!")

    def start(self):
        self.create_path()
        self.check_for_new_files()

    def get_data(self):
        return "Implemented!"

    def transform_data_to_df(self):
        return "Implemented!"


print(FilesSources())
