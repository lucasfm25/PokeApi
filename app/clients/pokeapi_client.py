import httpx

class PokeApiClient:
    BASE_URL = "https://pokeapi.co/api/v2"
    async def get(self, endpoint: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()