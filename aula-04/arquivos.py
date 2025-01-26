import csv
import os


def abrir_arquivo(arquivo: str) -> list:
    arquivo_csv: list = []

    caminho_do_arquivo: str = os.getcwd() + "/" + arquivo

    with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor_csv = csv.DictReader(arquivo)

        for linha in leitor_csv:
            arquivo_csv.append(linha)
            
    return arquivo_csv

print(abrir_arquivo("exemplo.csv"))
