
function addAluno(x, y, z){
    const aluno = {
        nome : x,
        idade : y,
        media : z
    };
    /*alert(`${aluno.nome} Adicionado!`);*/
    return aluno;
}
/******************************************   Essa função é igual, só que compacta
function addAluno(nome, idade, media){
    const aluno = {nome, idade, media};
    alert(`${aluno.nome} Adicionado!`);
    return aluno;
}
*/

const alunos = [];

alunos.push(addAluno('joao', 18, 8));
alunos.push(addAluno('maria', 19, 9));
alunos.push(addAluno('jose', 16, 10));
alunos.push(addAluno('feliphe', 27, 7));

console.log(alunos);
