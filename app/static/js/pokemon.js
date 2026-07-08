async function listarPokemons() {

    const response = await fetch("/pokemon");
    const pokemons = await response.json();
    const container = document.getElementById("pokemon-list");
    container.innerHTML = "";

    pokemons.forEach(pokemon => {
        const card = criarCardPokemon(pokemon);
        container.appendChild(card);
    });
}

function criarCardPokemon(pokemon) {

    const card = document.createElement("div");

    card.classList.add("pokemon-card");

    card.innerHTML = `
        <img
            src="${pokemon.imagem}"
            alt="${pokemon.name}"
        >

        <h3>${pokemon.name}</h3>

        <span>#${pokemon.id}</span>
    `;

    return card;

}