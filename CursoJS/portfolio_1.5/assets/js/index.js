function escopo() {
    document.addEventListener("DOMContentLoaded", function () {
        const navGestaoTarefas = document.getElementById("nav-gestaoTarefas");
        const navRedirectPage = document.getElementById("nav-redirectPage");

        // Function to execute when any of the links is clicked
        function handleNavLinkClick(event) {
            // Prevent the default behavior of the anchor link
            event.preventDefault();

            // Get the href attribute to determine which link was clicked
            const linkId = event.target.getAttribute("id");

            // Execute different actions based on the clicked link
            if (linkId === "nav-gestaoTarefas") {
                // Execute function for "Gestão de Tarefas"
                console.log("Gestão de Tarefas link clicked");

            }else if (linkId === "nav-redirectPage") {
                // Execute function for "Redirect Page"
                console.log("Redirect Page link clicked");
            }
        }

        // Add click event listeners to the links
        navGestaoTarefas.addEventListener("click", handleNavLinkClick);
        navRedirectPage.addEventListener("click", handleNavLinkClick);
    });

}
escopo();
