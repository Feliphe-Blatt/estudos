let alunos = ['joao', 'maria', 'jose'];

const novoAluno = prompt('Adicione um aluno:');
alunos.push(novoAluno);

document.body.innerHTML = `<br/>Lista de Alunos: '<b>${alunos}</b>'<br/>`;
console.log(alunos);

alunos.unshift('Cicrano');
alunos.unshift('fulano');

document.body.innerHTML += `<br/>Lista de Alunos: '<b>${alunos}</b>'<br/>`;
console.log(alunos);

let alunoRemovido = alunos.pop();
document.body.innerHTML += `<br/>Aluno Removido: '<b>${alunoRemovido}</b>'<br/>`;
console.log(alunoRemovido);


alunoRemovido = alunos.shift();
document.body.innerHTML += `<br/>Aluno removido: '<b>${alunoRemovido}</b>'<br/>`;
console.log(alunoRemovido);

document.body.innerHTML += `<br/>Lista de Alunos: '<b>${alunos}</b>'<br/>`;
console.log(alunos);

delete alunos[1];

document.body.innerHTML += `<br/>Alunos[1] depois de 'delete': '<b>${typeof(alunos[1])}</b>'<br/>`;
console.log(typeof(alunos[1]));

document.body.innerHTML += `<br/>Lista de Alunos: '<b>${alunos}</b>'<br/>`;
console.log(alunos);
