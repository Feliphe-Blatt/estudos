function escopo() {
    document.addEventListener("DOMContentLoaded", function () {
        const navInicio = document.getElementById("nav-inicio");
        const navGestaoTarefas = document.getElementById("nav-gestaoTarefas");
        const navRedirectPage = document.getElementById("nav-redirectPage");
        const modal = document.querySelector("#modal");

        function trocaSite(event) {
            event.preventDefault();

            const linkId = event.target.getAttribute("id");

            if (linkId === "nav-inicio") {
                console.clear();
                console.log("Início");

            } else if (linkId === "nav-gestaoTarefas") {
                console.clear();
                console.log("Gestão de Tarefas");

            } else if (linkId === "nav-redirectPage") {
                console.clear();
                console.log("Redirect Page");

            }
        }

        navInicio.addEventListener("click", trocaSite);
        navGestaoTarefas.addEventListener("click", trocaSite);
        navRedirectPage.addEventListener("click", trocaSite);
    });
}
escopo();
