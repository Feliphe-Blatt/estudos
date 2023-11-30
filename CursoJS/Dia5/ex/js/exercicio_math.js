const numeroInicial = parseFloat(prompt('Digite um número:'));

const num = document.getElementById('numero');  // Vinculando id's do html às variáveis no documento JS
const numTeste = document.getElementById('teste');
const numInteiro = document.getElementById('inteiro');
const numRaiz = document.getElementById('raiz');
const numCima = document.getElementById('cima');
const numBaixo = document.getElementById('baixo');
const numCasaDecimal = document.getElementById('decimal');

num.innerHTML = numeroInicial;

numTeste.innerHTML = !(Number.isNaN(numeroInicial)); // Operador booleano necessário para não inverter a resposta

numInteiro.innerHTML = Number.isInteger(numeroInicial);

numRaiz.innerHTML = numeroInicial**0.5; // Qualquer número elevado a 0.5 está sendo realizada a conta de raiz QUADRADA

numCima.innerHTML = Math.ceil(numeroInicial);

numBaixo.innerHTML = Math.floor(numeroInicial);

numCasaDecimal.innerHTML = numeroInicial.toFixed(2);
