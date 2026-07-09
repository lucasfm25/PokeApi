from fastapi import APIRouter
from app.services.evolution_service import EvolutionService

router = APIRouter(
    prefix="/evolution",
    tags=["Evolution"]
)

service = EvolutionService()

@router.get("/{id}")
async def busca_evolucao(id: int):
    return await service.busca_evolucao(id)

@router.get("/buscaIDEvolucao/{pokemon}")
async def busca_id_evolucao(pokemon: str):
    return await service.busca_id_evolucao(pokemon)