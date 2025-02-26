import asyncio
import json
import re
from math import ceil

import requests
from alive_progress import alive_it, config_handler
from bs4 import BeautifulSoup

config_handler.set_global(length=40)


def remove_circular_refs(ob, _seen=None):
    if _seen is None:
        _seen = set()
    if id(ob) in _seen:
        # circular reference, remove it.
        return None
    _seen.add(id(ob))
    res = ob
    if isinstance(ob, dict):
        res = {
            remove_circular_refs(k, _seen): remove_circular_refs(v, _seen)
            for k, v in ob.items()
        }
    elif isinstance(ob, (list, tuple, set, frozenset)):
        res = type(ob)(remove_circular_refs(v, _seen) for v in ob)
    # remove id again; only *nested* references count
    _seen.remove(id(ob))
    return res


def get_dados(item, field: str, context="dados"):
    if (
        item.find(class_=context) is not None
        and item.find(class_=context).find(class_=field) is not None
    ):
        return item.find(class_=context).find(class_=field)


async def get_all_images(pageUrl):
    response = requests.get(pageUrl)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        images = (
            soup.find(id="fotos_imovel")
            .find(id="swiper_fotos")
            .find(id="wrapper")
            .find_all("div", class_="swiper-slide")
        )
        source_images = []
        for image in images:
            source_images.append(image.find("img")["data-src"])

        return source_images


async def extract_data_from(pageUrl, get_qtd_registros=False):
    # Faz a requisição para obter o conteúdo da página
    response = requests.get(pageUrl)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscar quantidade de registros
        if get_qtd_registros:
            return int(soup.find(id="count").text)

        # Buscar todos os imoveis
        data = soup.find(class_="todos_imoveis").find_all("div", class_="resultado")

        for item in data:
            imovel_dict = {}

            if item.find(class_="foto").find("img").get("src") is not None:
                imovel_dict.update(
                    foto=item.find(class_="foto").find("img").get("src").strip()
                )

            if get_dados(item, "tipo") is not None:
                imovel_dict.update(titulo=get_dados(item, "tipo").text.strip())

            if get_dados(item, "localizacao") is not None:
                imovel_dict.update(bairro=get_dados(item, "localizacao").text.strip())

            if get_dados(item, "detalhes") is not None:
                detalhes = re.sub(
                    r"(\d+)", r" | \1", get_dados(item, "detalhes").text
                ).split("|")
                detalhes = list(filter(lambda s: s != " ", detalhes))
                detalhes = list(map(lambda s: s.strip(), detalhes))
                imovel_dict.update(resumo=detalhes)

            if get_dados(item, "alinha_valores") is not None:
                imovel_dict.update(
                    tipo=get_dados(item, "alinha_valores")
                    .find(class_="valor")
                    .find("small")
                    .text.strip()
                )

            if get_dados(item, "alinha_valores") is not None:
                imovel_dict.update(
                    preco=get_dados(item, "alinha_valores")
                    .find(class_="valor")
                    .find("h5")
                    .text.strip()
                )

            if get_dados(item, "alinha_valores") is not None:
                imovel_dict.update(
                    referencia=get_dados(item, "alinha_valores")
                    .find(class_="referencia")
                    .text.strip()
                )

            if get_dados(item, "descricao") is not None:
                imovel_dict.update(descricao=get_dados(item, "descricao").text.strip())

            if item.parent.get("href") is not None:
                detail_page = item.parent.get("href").strip()
                imovel_dict.update(link=detail_page)
                imovel_dict.update(
                    gallery=await get_all_images(
                        f"https://www.olafranca.com.br{detail_page}"
                    )
                )

            if imovel_dict.keys():
                imoveis.append(imovel_dict)

        return imoveis

    else:
        print(f"Erro ao acessar o site: {response.status_code}")


imoveis = []


async def main():
    negocios = ["alugar", "comprar"]

    for negocio in negocios:
        page = f"https://olafranca.com.br/{negocio}"
        total_registros = await extract_data_from(page, True)
        items_por_pagina = 12
        limit = ceil(total_registros / items_por_pagina) + 1
        # limit = 2

        bar = alive_it(range(1, limit), finalize=lambda bar: bar.text("All done!\n\n"))
        for i in bar:
            page = f"{page}/pagina-{i}"
            result = await extract_data_from(page)
            imoveis.append(result)
            bar.text(f"Getting page {i}...")

        with open(f"{negocio}.json", "w") as f:
            json.dump(remove_circular_refs(imoveis), f, indent=2, ensure_ascii=False)
            imoveis.clear()


asyncio.run(main())
