import json
import re

# Open and read the JSON file
with open("comprar.json", "r") as file:
    data = json.load(file)


# Print the data
for imovel in data:
    if imovel is not None:
        print(f"TITULO_AQUI: {imovel['titulo']} para {imovel['tipo']}")
        print(f"RESUMO_AQUI: {" ".join(imovel['resumo'])}")

        print(f"BAIRRO_AQUI: {imovel['bairro']}")
        print(f"PRECO_AQUI: {imovel['preco']}")
        print(f"URL_AQUI: http://www.olafranca.com.br{imovel['link']}")
        descricao = re.sub(r"(\n+)", r" ", imovel["descricao"])
        descricao = re.sub(r"(\?\?+)", r" ", descricao)
        print(f"DESCRICAO_AQUI: {descricao.strip()}")
        print(f"COD_REF_AQUI: {imovel['referencia']}")
        print(f"FOTO_AQUI: {imovel['foto']}")
        print(f"\n\n\n{"-"*50}\n\n\n")
