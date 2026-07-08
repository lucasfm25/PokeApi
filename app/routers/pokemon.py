from fastapi import APIRouter
from app.services.pokemon_service import PokemonService

router = APIRouter(
    prefix="/pokemon",
    tags=["Pokemon"]
)

service = PokemonService()

@router.get("/")
async def listar_pokemons():
    return await service.listar_pokemons()

@router.get("/{name}")
async def buscar_pokemon(name: str):
    return await service.buscar_pokemon(name)