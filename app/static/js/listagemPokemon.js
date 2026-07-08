async function buscarPokemon() {
    const nome = document.getElementById("pokemon-input").value;
    if (!nome)
        return;
    const response = await fetch(`/pokemon/${nome}`);
    if (!response.ok) {
        alert("Pokémon não encontrado.");
        return;
    }
    const pokemon = await response.json();
    renderizarPokemon(pokemon);
}

function renderizarPokemon(pokemon){

    const container = document.getElementById("pokemon-result");

    container.innerHTML = `

        <div class="pokemon-container">

            <div class="pokemon-image-card">

                <img
                    src="${pokemon.imagem}"
                    alt="${pokemon.nome}"
                >

            </div>

            <div class="pokemon-info-card">

                <div class="pokemon-info-left">

                    <h2>${pokemon.nome}</h2>

                    <p>#${pokemon.id}</p>

                    <hr>

                    <br>

                    <p><strong>Tipos</strong></p>
                    <p>${pokemon.tipos.join(", ")}</p>

                    <br>

                    <p><strong>Altura</strong></p>
                    <p>${pokemon.altura}</p>s

                    <br>

                    <p><strong>Peso</strong></p>
                    <p>${pokemon.peso}</p>

                    <br>

                    <p><strong>Habilidades</strong></p>

                    <ul>
                        ${pokemon.habilidades.map(h => `<li>${h}</li>`).join("")}
                    </ul>

                </div>

                <div class="pokemon-info-right">

                    <h3>Status Base</h3>

                    ${Object.entries(pokemon.stats).map(([nome, valor]) => `

                        <div class="stat">

                            <div class="stat-header">

                                <span>${formatarStat(nome)}</span>

                                <span>${valor}</span>

                            </div>

                            <div class="stat-bar">

                                <div
                                    class="stat-fill"
                                    style="width:${valor / 255 * 100}%"
                                ></div>

                            </div>

                        </div>

                    `).join("")}

                </div>

            </div>

            <div class="pokemon-evolution-card">

                <h2>Linha Evolutiva</h2>

                <p>Em desenvolvimento...</p>

            </div>

        </div>

    `;
}

function formatarStat(stat){

    const nomes = {

        "hp": "Hp",

        "attack": "Attack",

        "defense": "Defense",

        "special-attack": "Special Attack",

        "special-defense": "Special Defense",

        "speed": "Speed"

    };

    return nomes[stat] || stat;

}