function escopo() {
    document.addEventListener("DOMContentLoaded", function () {
        const navInicio = document.getElementById("nav-inicio");
        const navGestaoTarefas = document.getElementById("nav-gestaoTarefas");
        const navRedirectPage = document.getElementById("nav-redirectPage");
        const navContato = document.getElementById("nav-contato");

        function trocaSite(event) {
            event.preventDefault();

            const linkId = event.target.getAttribute("id");

            if (linkId === "nav-inicio") {
                console.log("Início");

            } else if (linkId === "nav-gestaoTarefas") {
                console.log("Gestão de Tarefas");

            } else if (linkId === "nav-redirectPage") {
                console.log("Redirect Page");
                
            }
        }

        navInicio.addEventListener("click", trocaSite);
        navGestaoTarefas.addEventListener("click", trocaSite);
        navRedirectPage.addEventListener("click", trocaSite);
        navContato.addEventListener("click", trocaSite);
    });
}
escopo();
