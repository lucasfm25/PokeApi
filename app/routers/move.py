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

@router.get("/{name}")
async def buscar_move(name: str):
    return await service.buscar_move(name)