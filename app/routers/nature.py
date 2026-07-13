from fastapi import APIRouter
from app.services.nature_service import NatureService

router = APIRouter(
    prefix="/nature",
    tags=["Nature"]
)

service = NatureService()

@router.get("/")
async def listar_natures():
    return await service.listar_natures()

@router.get("/{nature}")
async def busca_natures(nature: str):
    return await service.busca_natures(nature)