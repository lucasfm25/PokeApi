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

@router.get("/{regiao}")
async def buscar_regiao(regiao: str):
    return await service.buscar_regiao(regiao)

@router.get("/localidades/{regiao}")
async def busca_localidades(regiao: str):
    return await service.busca_localidades(regiao)