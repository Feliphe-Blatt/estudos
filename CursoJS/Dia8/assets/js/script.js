
function escopo (){
    const formulario = document.querySelector('#formulario');
    let contador = 1;
    /*
    formulario.onsubmit = function (evento){
        alert('formulário enviado!');
    };
    */
    function getFormulario(evento){

        // const genero = formulario.querySelector('#');
        const nascimento = formulario.querySelector('#nascimento');
        const correio = formulario.querySelector('#correio');
        const senha = formulario.querySelector('#senha');
        const cor = formulario.querySelector('#cor');
        const red = formulario.querySelector('#red');
        const green = formulario.querySelector('#green');
        const blue = formulario.querySelector('#blue');

        evento.preventDefault();
        alert(`Formulário de n° ${contador} "enviado!"`);
        console.log(`Formulário de n°: ${contador}`);
        contador++;
    }

    formulario.addEventListener('submit', getFormulario);
}

escopo();
