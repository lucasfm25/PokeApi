from app.clients.pokeapi_client import PokeApiClient

class PokemonService:
    def __init__(self):
        self.client = PokeApiClient()

    async def listar_pokemons(self):
        pokedex = await self.client.get("pokemon?limit=151")
        pokemons = []
        for pokemon in pokedex["results"]:
            pokemon_id = pokemon["url"].split("/")[-2]
            pokeomon_formatado = {
                "id": int(pokemon_id),
                "name": pokemon["name"].capitalize(),
                "imagem": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
            }
            pokemons.append(pokeomon_formatado)
        return pokemons
    
    async def buscar_pokemon(self, name: str):
        pokemon = await self.client.get(f"pokemon/{name.lower()}")

        tipos = []

        for tipo in pokemon["types"]:
            tipos.append(
                tipo["type"]["name"].capitalize()
            )

        habilidades = []

        for habilidade in pokemon["abilities"]:
            habilidades.append(
                habilidade["ability"]["name"].capitalize()
            )

        stats = {}

        for stat in pokemon["stats"]:
            stats[stat["stat"]["name"]] = stat["base_stat"]

        pokemon_species = await self.client.get(f"pokemon-species/{pokemon['id']}")

        pokemon_evolution_chain = await self.busca_evolucao(pokemon_species["evolution_chain"]["url"].split("/")[-2])

        return {
            "id": pokemon["id"],
            "nome": pokemon["name"].capitalize(),
            "imagem": pokemon["sprites"]["other"]["official-artwork"]["front_default"],
            "altura": f"{pokemon['height'] / 10} m",
            "peso": f"{pokemon['weight'] / 10} kg",
            "tipos": tipos,
            "habilidades": habilidades,
            "stats": stats,
            "linha_evolucao": pokemon_evolution_chain
        }
    
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
        