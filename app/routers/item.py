from fastapi import APIRouter
from app.services.item_service import ItemService

router = APIRouter(
    prefix="/item",
    tags=["Item"]
)

service = ItemService()

@router.get("/")
async def listar_itens():
    return await service.listar_itens()

@router.get("/{item}")
async def busca_itens(item: str):
    return await service.busca_itens(item)