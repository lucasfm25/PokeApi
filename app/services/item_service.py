from app.clients.pokeapi_client import PokeApiClient

class ItemService:
    def __init__(self):
        self.client = PokeApiClient()
    
    async def listar_itens(self):
        itens = await self.client.get("item")
        itens_formatadas = []
        for item in itens["results"]:
            item_id = item["url"].split("/")[-2]
            item_formatada = {
                "id": int(item_id),
                "name": item["name"].capitalize()
            }
            itens_formatadas.append(item_formatada)
        return itens_formatadas
    
    async def busca_itens(self, name: str):
        item = await self.client.get(f"item/{name.lower()}")
        atributos = []
        for atributo in item["attributes"]:
            atributos.append({
                "id" : atributo["url"].split("/")[-2],
                "name" : atributo["name"]
            })
            
        return {
                "id" : item["id"],
                "name" : item["name"],
                "cost" : item["cost"],
                "effect" : item["effect_entries"][1]["short_effect"].capitalize(),
                "image" : item["sprites"]["default"],
                "attributes" : atributos
                }