function addAluno(){
    const aluno = prompt('Adicione o novo aluno:');
    alert('Aluno adicionado!');
    return aluno;
}

const alunos = ['joao', 'maria', 'jose'];

alunos.push(addAluno());

const lista = document.getElementById('lista');
lista.innerHTML = alunos;
