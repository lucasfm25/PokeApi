from fastapi import APIRouter
from app.services.ability_service import AbilityService

router = APIRouter(
    prefix="/ability",
    tags=["Ability"]
)

service = AbilityService()

@router.get("/")
async def listar_abilitys():
    return await service.listar_abilitys()

@router.get("/{ability}")
async def busca_ability(ability: str):
    return await service.busca_ability(ability)