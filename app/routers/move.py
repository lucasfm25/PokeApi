from fastapi import APIRouter
from app.services.move_service import MoveService

router = APIRouter(
    prefix="/move",
    tags=["Move"]
)

service = MoveService()

@router.get("/")
async def listar_moves():
    return await service.listar_moves()

@router.get("/{move}")
async def buscar_move(move: str):
    return await service.buscar_move(move)

@router.get("/BuscaMovesPokemon/{pokemon}")
async def buscar_move_pokemon(pokemon: str):
    return await service.buscar_move_pokemon(pokemon)