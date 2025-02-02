import csv
from pathlib import Path


def read_csv(file_name: str) -> list[dict]:
    """
    efetua a leitura de arquivos csv
    """
    file_path = str(Path.cwd()) + "/" + file_name
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def processing_data(data: list[dict] = []) -> list[dict]:
    """
    modifica o dict produto adicionado o total de estoque de cada item
    """
    for product in range(len(data)):
        total: float = float(data[product]["preco"]) * float(data[product]["quant"])
        data[product]["total"] = total
    return data


def filter_delivered(data: list[dict] = []) -> list[dict]:
    """
    filtra relacao de produtos entregues
    """
    return list(filter(lambda product: product.get("entregue") == "True", data))


def filter_sum_totals(data: list[dict] = []) -> list[dict]:
    """
    soma o total dos produtos
    """
    total = 0
    for product in data:
        total += product.get("total")
    return total
