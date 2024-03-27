const pessoas = [
    { nome: "Feliphe", idade: 28 },
    { nome: "Cristiane", idade: 48 },
    { nome: "Jair", idade: 50 },
    { nome: "Elias", idade: 70 },
    { nome: "Júlia", idade: 68 },
    { nome: "Pedro", idade: 37 }
];

pessoas.forEach(function (valor, indice, array) {
    console.log(`\nNome: ${valor.nome}\nIdade: ${valor.idade}\nPosição na lista: ${indice + 1}ª`);
});