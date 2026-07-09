from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers.pokemon import router as pokemon_router
from app.routers.region import router as region_router
from app.routers.move import router as move_router
from app.routers.evolution import router as evolution_router
from app.routers.berry import router as berry_router

app = FastAPI(
    title="PokeAPI Hub",
    description="Hub para consultas da PokeAPI",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

#rotas
app.include_router(pokemon_router)
app.include_router(region_router)
app.include_router(move_router)
app.include_router(evolution_router)
app.include_router(berry_router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
    
@app.get("/pokemons")
async def pokemons(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pokemon.html"
    )

@app.get("/shiny")
async def shiny(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shiny.html"
    )

@app.get("/move")
async def move(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="move.html"
    )

@app.get("/berry")
async def move(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="berry.html"
    )