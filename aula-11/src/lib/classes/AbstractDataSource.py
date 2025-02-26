from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError("Method not implemented!")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Method not implemented!")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Method not implemented!")
