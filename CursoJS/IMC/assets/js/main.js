function escopo() {
    let contador = 1;
    const formulario = document.querySelector('#formulario');

    const formularios = [];

    
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////
    function getIMC(evento) {
        evento.preventDefault();

        /////////////////////////////////////// Altera nome, caso não exista mantém (sem nome)
        function validaNome(a) {
            let retornaNome = (a != '') ? a : '(Sem Nome)';

            return retornaNome;
        }

        /////////////////////////////////////// Confere se peso é válido
        function conferePeso(a) {
            if (!a.peso) {
                alert('Entrada de peso inválida!');
                return null;
            } else {
                return a.peso;
            }
        }

        /////////////////////////////////////// Confere se altura é válida
        function confereAltura(a) {
            if (!a.altura) {
                alert('Entrada de altura inválida!');
                return null;
            } else {
                return a.altura;
            }
        }

        /////////////////////////////////////// Faz teste de altura e peso, retornando o perfil caso seja válido
        function validaPessoa(a) {
            const testePeso = conferePeso(a);
            const testeAltura = confereAltura(a);

            if (testePeso && testeAltura) {
                resultadoTabela(a);
                return a;
            } else {
                return 'Entrada inválida!';
            }
        }

        /////////////////////////////////////// Altera nome, caso não exista mantém (sem nome)
        function setNome(a) {
            let retornaNome = (a.nome != '') ? a.nome : '(Sem Nome)';

            return retornaNome;
            /*
                if(a.nome != ''){
                    return a.nome;
                }else {
                    return '(Sem Nome)';
                }
            */
        }

        /////////////////////////////////////// Altera a cor da tabela de acordo com resultado
        function corTabela(a, b, c, d, e, f, g) {

            const verde = "#0de71c";
            const branco = "#ffffff";

            // Limpa cores
            b.style.backgroundColor = branco;
            c.style.backgroundColor = branco;
            d.style.backgroundColor = branco;
            e.style.backgroundColor = branco;
            f.style.backgroundColor = branco;
            g.style.backgroundColor = branco;

            // Pinta o fundo do resultado de verde            
            if (a < 18.5) {
                b.style.backgroundColor = verde;
            } else if (a <= 24.9) {
                c.style.backgroundColor = verde;
            } else if (a <= 29.9) {
                d.style.backgroundColor = verde;
            } else if (a <= 34.9) {
                e.style.backgroundColor = verde;
            } else if (a <= 39.9) {
                f.style.backgroundColor = verde;
            } else {
                g.style.backgroundColor = verde;
            }
        }

        /////////////////////////////////////// Escolhe veredito de acordo com resultado
        function vereditoTabela(a) {
            const nivel = ['Abaixo do peso', 'Peso normal', 'Sobrepeso', 'Obesidade grau 1', 'Obesidade grau 2', 'Obesidade grau 3'];
            if (a < 18.5) return nivel[0];
            if (a <= 24.9) return nivel[1];
            if (a <= 29.9) return nivel[2];
            if (a <= 34.9) return nivel[3];
            if (a <= 39.9) return nivel[4];
            if (a > 39.9) return nivel[5];
        }

        /////////////////////////////////////// Troca resultado na tabela e altera a cor
        function resultadoTabela(a) {
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
            imc.innerHTML = resultado;
            veredito.innerHTML = vereditoTabela(resultado);
            corTabela(resultado, opcao1, opcao2, opcao3, opcao4, opcao5, opcao6);
        }

        /////////////////////////////////////// Cria o 'perfil' e mostra resultado
        function addFormulario(a, b, c) {

            const pessoa = {

                nome: validaNome(a),
                peso: b,
                altura: c,

                imc() {
                    let temporario = 0;
                    temporario = (this.peso / (this.altura ** 2));
                    return temporario.toFixed(1);
                }
            };

            return validaPessoa(pessoa);
        }

        /////////////////////////////////////// Exibe histórico temporário dos cálculos realizados no console.log()
        function historico(form) {
            console.clear();
            console.log('//////////////////////////////////////////////////////////////////////////////////////');
            for (let i = 0; i < form.length; i++) {
                console.log(`\n/////////////////> Registro n°: ${i+1}`);
                console.log(`Nome: ${form[i].nome};`);
                console.log(`Peso: ${form[i].peso};`);
                console.log(`Altura: ${form[i].altura};`);
                console.log(`IMC: ${form[i].imc()};`);
                console.log(`Veredito: ${vereditoTabela(form[i].imc())}\n`);
            }
            console.log('\n//////////////////////////////////////////////////////////////////////////////////////');
        }

        const nome = formulario.querySelector('#nome');
        const peso = formulario.querySelector('#peso');
        const altura = formulario.querySelector('#altura');

        formularios.push(addFormulario(nome.value, Number(peso.value), Number(altura.value)));
        historico(formularios);
    }

    formulario.addEventListener('submit', getIMC);
}

escopo();
