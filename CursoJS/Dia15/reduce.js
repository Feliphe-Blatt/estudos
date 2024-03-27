const numeros = [1, 3, 2, 6, 5, 9, 14, 29, 43, 94];

const total = numeros.reduce(function (soma, valor, i, arr) {
    soma += valor;
    return soma;
}, 0);

const pessoas = [
    { nome: "Feliphe", idade: 28 },
    { nome: "Cristiane", idade: 48 },
    { nome: "Jair", idade: 50 },
    { nome: "Elias", idade: 70 },
    { nome: "Júlia", idade: 68 },
    { nome: "Pedro", idade: 37 }
];

const maisVelha = pessoas.reduce(function (inicial, proximo) {

    if (inicial.idade > proximo.idade) return inicial;

    return proximo;
});
console.log(maisVelha.nome);
