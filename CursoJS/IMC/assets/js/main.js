function escopo (){
    let contador = 1;
    const formulario = document.querySelector('#formulario');
    
    const formularios = [];

    //////////////////////////////////////////////////////////////////////////////////////////////////////////////
    function getIMC(evento){
        evento.preventDefault();

        /////////////////////////////////////// Confere se peso é válido
        function conferePeso(a){
            if(!a.peso){
                alert('Entrada de peso inválida!');
                return null;
            }else {
                return a.peso;
            }
        }

        /////////////////////////////////////// Confere se altura é válida
        function confereAltura(a){
            if(!a.altura){
                alert('Entrada de altura inválida!');
                return null;
            }else {
                return a.altura;
            }
        }

        /////////////////////////////////////// Faz teste de altura e peso, retornando o perfil caso seja válido
        function validaPessoa(a){
            const testePeso = conferePeso(a);
            const testeAltura = confereAltura(a);
            
            if (testePeso && testeAltura){
                resultadoTabela(a);
                return a;
            }else {
                return 'Entrada inválida!';
            }
        }

        /////////////////////////////////////// Altera nome, caso não exista mantém sem nome
        function setNome(a){
            if(a.nome != ''){
                return a.nome;
            }else {
                return '(Sem Nome)';
            }
        }

        /////////////////////////////////////// Altera a cor da tabela de acordo com resultado
        function corTabela(a, b, c, d, e, f, g){
            if (a < 18.5){
                b.style.backgroundColor = "#0de71c";
                c.style.backgroundColor = "#ffffff";
                d.style.backgroundColor = "#ffffff";
                e.style.backgroundColor = "#ffffff";
                f.style.backgroundColor = "#ffffff";
                g.style.backgroundColor = "#ffffff";
    
            }else if((a >= 18.5) && (a <= 24.9)){
                b.style.backgroundColor = "#ffffff";
                c.style.backgroundColor = "#0de71c";
                d.style.backgroundColor = "#ffffff";
                e.style.backgroundColor = "#ffffff";
                f.style.backgroundColor = "#ffffff";
                g.style.backgroundColor = "#ffffff";
    
            }else if((a > 24.9) && (a <= 29.9)){
                b.style.backgroundColor = "#ffffff";
                c.style.backgroundColor = "#ffffff";
                d.style.backgroundColor = "#0de71c";
                e.style.backgroundColor = "#ffffff";
                f.style.backgroundColor = "#ffffff";
                g.style.backgroundColor = "#ffffff";
    
            }else if((a > 29.9) && (a <= 34.9)){
                b.style.backgroundColor = "#ffffff";
                c.style.backgroundColor = "#ffffff";
                d.style.backgroundColor = "#ffffff";
                e.style.backgroundColor = "#0de71c";
                f.style.backgroundColor = "#ffffff";
                g.style.backgroundColor = "#ffffff";
    
            }else if((a > 34.9) && (a <= 39.9)){
                b.style.backgroundColor = "#ffffff";
                c.style.backgroundColor = "#ffffff";
                d.style.backgroundColor = "#ffffff";
                e.style.backgroundColor = "#ffffff";
                f.style.backgroundColor = "#0de71c";
                g.style.backgroundColor = "#ffffff";
    
            }else if(a > 39.9){
                b.style.backgroundColor = "#ffffff";
                c.style.backgroundColor = "#ffffff";
                d.style.backgroundColor = "#ffffff";
                e.style.backgroundColor = "#ffffff";
                f.style.backgroundColor = "#ffffff";
                g.style.backgroundColor = "#0de71c";
    
            }
        }

        /////////////////////////////////////// Escolhe veredito de acordo com resultado
        function vereditoTabela(a){
            if (a < 18.5) return 'Abaixo do peso';
            if(a <= 24.9) return 'Peso normal';
            if(a <= 29.9) return 'Sobrepeso';
            if(a <= 34.9) return 'Obesidade grau 1';
            if(a <= 39.9) return 'Obesidade grau 2';
            if(a > 39.9) return 'Obesidade grau 3';
        }
        
        /////////////////////////////////////// Troca resultado na tabela e altera a cor
        function resultadoTabela(a){
            const nome = document.getElementById('nomeTabela');
            const imc = document.getElementById('resultadoTabela');
            const veredito = document.getElementById('ver');
            const opcao1 = document.getElementById('op1');
            const opcao2 = document.getElementById('op2');
            const opcao3 = document.getElementById('op3');
            const opcao4 = document.getElementById('op4');
            const opcao5 = document.getElementById('op5');
            const opcao6 = document.getElementById('op6');

            nome.innerHTML = setNome(a);

            const resultado = a.imc();

            corTabela(resultado, opcao1, opcao2, opcao3, opcao4, opcao5, opcao6);

            imc.innerHTML = resultado;

            veredito.innerHTML = vereditoTabela(resultado);

        }

        /////////////////////////////////////// Cria o 'perfil' e mostra resultado
        function addFormulario(a, b, c){

            const pessoa = {
                nome : a,
                peso : b,
                altura : c,
                imc (){
                    let temporario = 0;
                    temporario = (this.peso / (this.altura**2));
                    return temporario.toFixed(1);
                }
            };
            return validaPessoa(pessoa);
        }

        const nome = formulario.querySelector('#nome');
        const peso = formulario.querySelector('#peso');
        const altura = formulario.querySelector('#altura');
        
        formularios.push(addFormulario(nome.value, Number(peso.value), Number(altura.value))); // Adição do perfil criado em 'addFormulario' na lista 'formularios' e mostra resultado com 'resultadoTabela'

        console.log(formularios);
    }
    
    formulario.addEventListener('submit', getIMC);
}

escopo();
