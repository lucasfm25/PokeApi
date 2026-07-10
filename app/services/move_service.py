from app.clients.pokeapi_client import PokeApiClient

class MoveService:
    def __init__(self):
        self.client = PokeApiClient()

    async def listar_moves(self):
        moves = await self.client.get("move")
        moves_formatadas = []
        for move in moves["results"]:
            move_id = move["url"].split("/")[-2]
            move_formatada = {
                "id": int(move_id),
                "name": move["name"].capitalize()
            }
            moves_formatadas.append(move_formatada)
        return moves_formatadas


    async def buscar_move(self, move_name: str):
        move = await self.client.get(f"move/{move_name.lower()}")
        pokemons = []

        for pokemon in move["learned_by_pokemon"]:
            pokemon_id = pokemon["url"].rstrip("/").split("/")[-1]
            pokemon_name = pokemon["name"].capitalize()
            pokemon_img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
            pokemon_formatado = {
                "id": int(pokemon_id),
                "name": pokemon_name,
                "image": pokemon_img
            }
            pokemons.append(pokemon_formatado)

        return {
            "id": move["id"],
            "name": move["name"].capitalize(),
            "type": move["type"]["name"].capitalize(),
            "power": move["power"],
            "accuracy": move["accuracy"],
            "priority": move["priority"],
            "pp": move["pp"],
            "damage_class": move["damage_class"]["name"].capitalize(),
            "effect_entries": [entry["effect"] for entry in move["effect_entries"] if entry["language"]["name"] == "en"],
            "pokemons": pokemons
        }
    
    async def buscar_move_pokemon(self, nome_pokemon: str):
        pokemon = await self.client.get(f"pokemon/{nome_pokemon.lower()}")
        pokemon_moves = []
        for simple_move in pokemon["moves"]:
            move = await self.client.get(f"move/{simple_move["move"]["name"]}")
            move_formatado = {
                "id": move["id"],
                "name": move["name"].capitalize(),
                "type": move["type"]["name"].capitalize(),
                "power": move["power"],
                "accuracy": move["accuracy"],
                "priority": move["priority"],
                "pp": move["pp"],
                "damage_class": move["damage_class"]["name"].capitalize(),
            }
            pokemon_moves.append(move_formatado)

        return pokemon_moves
