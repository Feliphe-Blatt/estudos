const numero = Number(prompt('Digite um número:'));

const realmente = Number.isNaN(numero);
const raiz = numero ** 0.5;
const inteiro = Number.isInteger(numero);
const baixo = Math.floor(numero);
const cima = Math.ceil(numero);
const decimais = numero.toFixed(2);

htmlNumero.innerHTML = numero;

if (!realmente) {
    htmlRealmente.innerHTML = 'Sim';
    htmlRaiz.innerHTML = raiz;
    if (inteiro) {
        htmlInteiro.innerHTML = 'Sim';
    } else {
        htmlInteiro.innerHTML = 'Não';
    }
    htmlBaixo.innerHTML = baixo;
    htmlCima.innerHTML = cima;
    htmlDecimais.innerHTML = decimais;
} else {
    htmlRealmente.innerHTML = 'Não';
}
