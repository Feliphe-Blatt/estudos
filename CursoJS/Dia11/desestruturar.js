
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const [num1, num2, num3, num4, num5, ...resto] = numeros;

const [copia1, , copia3, , copia5] = numeros;

const aluno = {
    nome: 'feliphe blatt',
    idade: 27,
    medias:{
        portugues: 7,
        matematica: 8,
        ingles: 10,
        literatura: 9
    }
};

function pegaNome(a){
    const {nome} = a;
    return nome;
}

function pegaIdade(a){
    const {idade} = a;
    return idade;
}

function pegaMedia(a, i){
    const {medias: {portugues: pt = 0, matematica: mat = 0, ingles: ing = 0, literatura: lit= 0}} = a;
    const med = [pt, mat, ing, lit];
    return med[i];
}

console.log(`
    Aluno: ${pegaNome(aluno)};\n
    Idade: ${pegaIdade(aluno)};\n
    medias:\n
        -> pt: ${pegaMedia(aluno, 0)};\n
        -> mat: ${pegaMedia(aluno, 1)};\n
        -> ing: ${pegaMedia(aluno, 2)};\n
        -> lit ${pegaMedia(aluno, 3)}.
`);
