window.alert('Mensagem de alerta!'); // retorna 'undefined'

window.confirm('Alerta de pergunta!'); // retorna 'true' or 'false'

const confirmacao = confirm('Verdadeiro ou falso?'); // guarda valor na constante

const inputUsuario = prompt('Digite algo pra guardar:'); //vai ser gravado como 'string'

alert(inputUsuario);

const numero1 = prompt('Digite um número:');
const numero2 = prompt('Digite outro número:');

const resultadoFinal = Number(numero1) + Number(numero2);

alert(`A soma de ${numero1} com ${numero2} é: ${resultadoFinal}`);