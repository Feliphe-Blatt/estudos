
function escopo (){
    let contador = 1;
    const formulario = document.querySelector('#formulario');
    const resultado = document.querySelector('#resultados');
    
    /*
    formulario.onsubmit = function (evento){
        alert('formulário enviado!');
    };
    */

    const formularios = [];

    function getFormulario(evento){
        evento.preventDefault();

        // Input de foto será adicionado em breve!

        const foto = formulario.querySelector('#arquivo');

        const nascimento = formulario.querySelector('#nascimento');

        const correio = formulario.querySelector('#correio');

        const senha = formulario.querySelector('#senha');

        const cor = formulario.querySelector('#cor');

        const red = formulario.querySelector('#red');
        const green = formulario.querySelector('#green');
        const blue = formulario.querySelector('#blue');

        // selecionaGenero: Confere qual gênero foi escolhido para enviar na resposta do formulário
        function selecionaGenero(){
            const gen1 = document.getElementById('gen1');
            const gen2 = document.getElementById('gen2');
            const genx = document.getElementById('genx');

            let temporario = '';
            if (gen1.checked){
                temporario = 'Masculino';
            }
            else if (gen2.checked) {
                temporario = 'Feminino';
            }
            else if (genx.checked){
                temporario = 'Outr@';
            }
            return temporario;
        }

        // addFormulario: Utilizado para gravar os resultados na lista completa de envios
        function addFormulario(a, b, c, d, e, f, g, h){
            const resultado = {
                nascimento : a,
                correio : b,
                senha : c,
                cor : d,
                red : e,
                green : f,
                blue : g,
                genero : h,

                alerta (){
                    alert(`Formulário de " ${this.correio} " enviado!`);
                }
            };
            resultado.alerta();
            return resultado;
        }

        // resumo: Atualiza a tabela ao fim do formulário com as respostas dadas pelo usuário
        function resumo(a, b, c, d, e, f, g, h){
            const nascimento = document.getElementById('a');
            const correio = document.getElementById('b');
            const senha = document.getElementById('c');
            const cor = document.getElementById('d');
            const red = document.getElementById('e');
            const green = document.getElementById('f');
            const blue = document.getElementById('g');
            const genero = document.getElementById('h');

            nascimento.innerHTML = a;
            correio.innerHTML = b;
            senha.innerHTML = c;
            cor.innerHTML = d;
            red.innerHTML = e;
            green.innerHTML = f;
            blue.innerHTML = g;
            genero.innerHTML = h;

        }

        formularios.push(addFormulario(nascimento.value, correio.value, senha.value, cor.value, red.value, green.value, blue.value, selecionaGenero()));

        resumo(nascimento.value, correio.value, senha.value, cor.value, red.value, green.value, blue.value, selecionaGenero());

        console.log(`Formulário de n°: ${contador}`);
        contador++;
        console.log(formularios);
    }
    formulario.addEventListener('submit', getFormulario);
}
escopo();
