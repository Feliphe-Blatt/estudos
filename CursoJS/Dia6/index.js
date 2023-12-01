let alunos = ['joao', 'maria', 'jose'];

const novoAluno = prompt('Adicione um aluno');

alunos.push(novoAluno);

document.body.innerHTML = `<br/><b>${alunos}</b><br/>`;
console.log(alunos)
