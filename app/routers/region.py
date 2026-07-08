from fastapi import APIRouter
from app.services.region_service import RegionService

router = APIRouter(
    prefix="/region",
    tags=["Region"]
)

service = RegionService()

@router.get("/")
async def listar_regioes():
    return await service.listar_regioes()

@router.get("/{name}")
async def buscar_regiao(name: str):
    return await service.buscar_regiao(name)