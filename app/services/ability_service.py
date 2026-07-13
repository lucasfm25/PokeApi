from app.clients.pokeapi_client import PokeApiClient

class AbilityService:
    def __init__(self):
        self.client = PokeApiClient()
    
    async def listar_abilitys(self):
        abilitys = await self.client.get("ability")
        abilitys_formatadas = []
        for ability in abilitys["results"]:
            ability_id = ability["url"].split("/")[-2]
            ability_formatada = {
                "id": int(ability_id),
                "name": ability["name"].capitalize()
            }
            abilitys_formatadas.append(ability_formatada)
        return abilitys_formatadas

    async def busca_ability(self, name: str):
        ability = await self.client.get(f"ability/{name.lower()}")
        pokemons_formatados = []
        for pokemon in ability["pokemon"]:
            pokemons_formatados.append({
                "id" : pokemon["pokemon"]["url"].split("/")[-2],
                "name" : pokemon["pokemon"]["name"].capitalize()
            })
        return {
                "id" : ability["id"],
                "name" : ability["name"],
                "effect" : ability["effect_entries"][1]["effect"].capitalize(),
                "pokemons" : pokemons_formatados
                }