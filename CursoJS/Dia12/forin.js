
const listaCompra = ['batata', 'maçã', 'uva', 'vinagre', 'pão', 'arroz', 'feijão'];

for( let i in listaCompra){
    console.log(listaCompra[i]);
}

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

for(let i in aluno){
    console.log(i, aluno[i]);
}
