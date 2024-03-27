// soma dos números pares dobrados
const numeros = [1, 3, 2, 6, 5, 9, 14, 29, 43, 94];

const somaParesDobrados = numeros
    .filter(valor => (valor % 2) === 0)
    .map(valor => valor * 2)
    .reduce(((acumulador, valor) => acumulador + valor), 0);

console.log(somaParesDobrados);