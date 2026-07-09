from app.clients.pokeapi_client import PokeApiClient

class EvolutionService:
    def __init__(self):
        self.client = PokeApiClient()

    async def busca_id_evolucao(self, name: str):
        pokemon = await self.client.get(f"pokemon/{name.lower()}")
        pokemon_species = await self.client.get(f"pokemon-species/{pokemon['id']}")
        return (pokemon_species["evolution_chain"]["url"].split("/")[-2])

    async def busca_evolucao(self, evolution_chain_id: int):
        evolucoes = await self.client.get(f"evolution-chain/{evolution_chain_id}")
        evolucao_formatada = []

        def formatar_evolucao(chain):

            pokemon_id = int(chain["species"]["url"].rstrip("/").split("/")[-1])

            evolucao_formatada.append({

                "id": pokemon_id,

                "nome": chain["species"]["name"].capitalize(),

                "imagem": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
            })

            for proxima in chain["evolves_to"]:
                formatar_evolucao(proxima)

        formatar_evolucao(evolucoes["chain"])
        return evolucao_formatada