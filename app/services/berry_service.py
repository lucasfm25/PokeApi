from app.clients.pokeapi_client import PokeApiClient

class BerryService:
    def __init__(self):
        self.client = PokeApiClient()

    async def listar_berries(self):
        berries = await self.client.get("berry")
        berries_formatadas = []
        for simple_berry in berries["results"]:
            berry_id = simple_berry["url"].split("/")[-2]
            berry = await self.client.get(f"berry/{berry_id}")
            berry_formatada = {
                "id": int(berry_id),
                "name": berry["name"].capitalize(),
                "image" : f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/{berry["name"]}.png",
                "type" : berry["natural_gift_type"]["name"]
            }
            berries_formatadas.append(berry_formatada)
        return berries_formatadas

