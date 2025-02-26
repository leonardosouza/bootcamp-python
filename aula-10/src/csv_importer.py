import os

import pandas as pd
from importer import Importer

# without classes
csv_file = "sales.csv"
df = pd.read_csv(f"{os.path.dirname(__file__)}/{csv_file}")
if df["entregue"] is True:
    product_delivered = df[df["entregue"]]

# with classes
df = Importer("sales.csv")
print("\n\n# Filtro por Produto")
print(df.load_from_csv().filter_by_collumn("produto", "keyboard").get_result())

print("\n\n# Filtro por Entregue")
print(df.load_from_csv().filter_by_collumn("entregue", True).get_result())

print("\n\n# Todos os dados")
print(df.load_from_csv().get_all_data())

print("\n\n# Duas colunas")
print(
    df.load_from_csv()
    .filter_by_collumn("quant", 10)
    .filter_by_collumn("entregue", False)
    .filter_by_collumn("preco", 300)
    .get_result()
)
