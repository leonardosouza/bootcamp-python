from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    em_estoque: bool
