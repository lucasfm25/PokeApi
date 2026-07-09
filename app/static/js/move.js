async function buscarMove(){

    const nome = document.getElementById("move-input").value;

    if(!nome)
        return;

    const response = await fetch(`/move/${nome}`);

    if(!response.ok){

        alert("Move não encontrado.");

        return;

    }

    const move = await response.json();

    renderizarMove(move);

}

function renderizarMove(move){

    const container = document.getElementById("move-result");

    container.innerHTML = `

        <div class="move-container">

            <div class="move-info-card">

                <h2>${move.name}</h2>

                <hr>

                <br>

                <p><strong>Tipo:</strong> ${move.type}</p>

                <p><strong>Classe:</strong> ${move.damage_class}</p>

                <p><strong>Poder:</strong> ${move.power}</p>

                <p><strong>Precisão:</strong> ${move.accuracy}</p>

                <p><strong>PP:</strong> ${move.pp}</p>

                <p><strong>Prioridade:</strong> ${move.priority}</p>

                <br>

                <p>${move.effect_entries[0]}</p>

            </div>

            <div class="move-pokemon-card">

                <h2>Pokémons que aprendem esse golpe</h2>

                <div class="pokemon-grid">

                    ${move.pokemons.map(pokemon => `

                        <div class="pokemon-card">

                            <img
                                src="${pokemon.image}"
                                alt="${pokemon.name}"
                            >

                            <h3>${pokemon.name}</h3>

                            <span>#${pokemon.id}</span>

                        </div>

                    `).join("")}

                </div>

            </div>

        </div>

    `;

}