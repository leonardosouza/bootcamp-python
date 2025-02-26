from fastapi import APIRouter, Depends
from models.item_model import Item
from services.auth_service import AuthService

router = APIRouter(prefix="/items", tags=["Items"])

items = []


@router.post("/")
async def criar_item(
    item: Item, current_user: str = Depends(AuthService.get_current_user)
):
    items.append(item)
    return {"item": item}


@router.get("/")
async def listar_items(current_user: str = Depends(AuthService.get_current_user)):
    return {"items": items}
