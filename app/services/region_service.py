from app.clients.pokeapi_client import PokeApiClient

class RegionService:
    def __init__(self):
        self.client = PokeApiClient()

    async def listar_regioes(self):
        regioes = await self.client.get("region")
        regioes_formatadas = []
        for regiao in regioes["results"]:
            regiao_id = regiao["url"].split("/")[-2]
            regiao_formatada = {
                "id": int(regiao_id),
                "name": regiao["name"].capitalize()
            }
            regioes_formatadas.append(regiao_formatada)
        return regioes_formatadas
    
    async def buscar_regiao(self, name: str):
        regiao = await self.client.get(f"region/{name.lower()}")

        pokedex_id = regiao["pokedexes"][0]["url"].rstrip("/").split("/")[-1]
        pokedex = await self.client.get(f"pokedex/{pokedex_id}")
        pokemons_regiao = []
        for pokemon in pokedex["pokemon_entries"]:
            pokemon_id = pokemon["entry_number"]
            pokemon_id_img = pokemon["pokemon_species"]["url"].rstrip("/").split("/")[-1]
            pokemons_regiao.append({
                "id": pokemon_id,
                "name": pokemon["pokemon_species"]["name"].capitalize(),
                "imagem": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/{pokemon_id_img}.png"
            })
        return {
            "id": regiao["id"],
            "name": regiao["name"].capitalize(),
            "pokemons": pokemons_regiao
        }