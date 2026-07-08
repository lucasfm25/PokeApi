const submenus = document.querySelectorAll(".submenu");

submenus.forEach(submenu => {

    const title = submenu.querySelector(".submenu-title");

    const items = submenu.querySelector(".submenu-items");

    const arrow = submenu.querySelector(".arrow");

    title.addEventListener("click", () => {

        items.classList.toggle("active");

        arrow.classList.toggle("open");

    });

});