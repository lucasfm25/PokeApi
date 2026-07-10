let todosMoves = [];

document.getElementById("move-filter").addEventListener("change", filtrarMoves);

async function buscarMovesPokemon(){

    const pokemon = document.getElementById("pokemon-input").value.trim();
    
    if(!pokemon)
        return;

    const response = await fetch(`move/BuscaMovesPokemon/${pokemon}`);

    const moves = await response.json();

    todosMoves = moves;

    renderizarMoves(todosMoves);

    if(!response.ok){

        alert("Pokémon não encontrado.");

        return;

    }

}

function renderizarMoves(moves){

    const container = document.getElementById("moves-result");

    container.innerHTML = "";

    moves.forEach(move => {

        container.innerHTML += `

            <div class="move-card">

                <h2>${move.name}</h2>

                <hr>

                <br>

                <p><strong>Tipo:</strong> ${move.type}</p>

                <p><strong>Classe:</strong> ${move.damage_class}</p>

                <p><strong>Poder:</strong> ${formatarValor(move.power)}</p>

                <p><strong>Precisão:</strong> ${formatarValor(move.accuracy)}</p>

                <p><strong>PP:</strong> ${move.pp}</p>

                <p><strong>Prioridade:</strong> ${move.priority}</p>

            </div>

        `;

    });

}

function formatarValor(valor){

    if(valor === null)
        return "--";

    return valor;

}

function filtrarMoves(){

    const filtro = document.getElementById("move-filter").value;

    if(filtro === "Todos"){

        renderizarMoves(todosMoves);

        return;

    }

    const filtrados = todosMoves.filter(move =>

        move.damage_class === filtro

    );

    renderizarMoves(filtrados);

}