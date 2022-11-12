const nome = 'Feliphe';
const sobreNome = 'Blatt';
const idade = 26;
const peso = 63;
const altura = 1.79;

let indiceMassaCorporea;
let nascimento;

indiceMassaCorporea = peso / (altura * altura);

nascimento = 2022 - idade;

console.log(`\nPaciente de nome: ${nome} ${sobreNome};`);
console.log(`Nascido em: ${nascimento};`);
console.log(`Tem ${idade} anos, ${peso}kg, e ${altura}m de altura;`);

console.log(`Este possui um IMC de: ${indiceMassaCorporea}.`);