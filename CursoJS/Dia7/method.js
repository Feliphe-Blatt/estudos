
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

const copiaAlunos = alunos; // Atribui mesmo endereço na memoria, como um novo 'atalho'.

const teste = {...alunos};  // Copia todos os valores para outro valor na memória, implicando na independência das variáveis

alunos.push(addAluno('gepeto', 30, 10));

console.log(copiaAlunos);

console.log(teste);
