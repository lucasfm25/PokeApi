from app.clients.pokeapi_client import PokeApiClient

class NatureService:
    def __init__(self):
        self.client = PokeApiClient()
    
    async def listar_natures(self):
        natures = await self.client.get("nature")
        natures_formatadas = []
        for nature in natures["results"]:
            nature_id = nature["url"].split("/")[-2]
            nature_formatada = {
                "id": int(nature_id),
                "name": nature["name"].capitalize()
            }
            natures_formatadas.append(nature_formatada)
        return natures_formatadas
    
    async def busca_natures(self, name: str):
        nature = await self.client.get(f"nature/{name.lower()}")
        return {
                "id" : nature["id"],
                "name" : nature["name"],
                "- stat" : nature["decreased_stat"]["name"].capitalize(),
                "+ stat" : nature["increased_stat"]["name"].capitalize(),
                "favorite flavor" : nature["likes_flavor"]["name"].capitalize(),
                "hated flavor" : nature["hates_flavor"]["name"].capitalize()
                }
