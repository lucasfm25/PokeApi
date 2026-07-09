from fastapi import APIRouter
from app.services.berry_service import BerryService

router = APIRouter(
    prefix="/berry",
    tags=["Berry"]
)

service = BerryService()

@router.get("/")
async def listar_berries():
    return await service.listar_berries()