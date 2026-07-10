async function listarBerries(){

    const response = await fetch("/berries");

    const berries = await response.json();

    const container = document.getElementById("berry-list");

    container.innerHTML = "";

    berries.forEach(berry => {

        container.appendChild(criarCardBerry(berry));

    });

}

function criarCardBerry(berry){

    const card = document.createElement("div");

    card.classList.add("berry-card");

    card.innerHTML = `

        <img
            src="${berry.image}"
            alt="${berry.name}"
        >

        <h3>${berry.name}</h3>

        <p><strong>Tipo:</strong> ${berry.type}</p>

    `;

    return card;

}

listarBerries();