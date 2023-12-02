
function addAluno(x, y, z){
    const aluno = {
        nome : x,
        idade : y,
        media : z,

        bemVindo (){
            alert(`Bem vindo a nossa turma ${this.nome}!`);
        }  
    };
    alert(`${aluno.nome} Adicionado!`);
    return aluno;
}

const alunos = [];

alunos.push(addAluno('joao', 18, 8));
alunos.push(addAluno('maria', 19, 9));
alunos.push(addAluno('jose', 16, 10));
alunos.push(addAluno('feliphe', 27, 7));

alunos[0].bemVindo();

console.log(alunos);
