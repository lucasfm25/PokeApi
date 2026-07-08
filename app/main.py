from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers.pokemon import router as pokemon_router

app = FastAPI(
    title="PokeAPI Hub",
    description="Hub para consultas da PokeAPI",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

#rotas
app.include_router(pokemon_router)

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