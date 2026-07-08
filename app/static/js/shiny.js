document.addEventListener("DOMContentLoaded", carregarRegioes);
async function carregarRegioes(){

    const response = await fetch("/region");

    const regioes = await response.json();

    const select = document.getElementById("region-select");

    regioes.forEach(regiao => {

        select.innerHTML += `

            <option value="${regiao.name}">

                ${regiao.name}

            </option>

        `;

    });

}

async function buscarRegiao(){

    const regiao = document.getElementById("region-select").value;

    if(!regiao)
        return;

    const response = await fetch(`/region/${regiao}`);

    const regiaoData = await response.json();

    const pokemons = regiaoData.pokemons;
    const container = document.getElementById("pokemon-result");
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
