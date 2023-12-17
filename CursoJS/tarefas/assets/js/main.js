function escopo() {

    ///////////////////////////////////////////////////////////////////////////  Adicionando tarefa


    function escreveTarefa(tarefa, i) {  //  Escrevendo tarefa no documento html

        if (typeof i === 'undefined') i = 'x';  //  Definindo valor padrão para 'i' caso não seja passado valor

        const tableRoll = document.createElement('tr');
        tableRoll.innerHTML = `
        <td>
            <h1 class="listItem" id="item-${i}">
                ${tarefa}
            </h1>
        </td>
        <td>
            <button class="list-edit" id="btn-edit-${i}" title="Editar a tarefa">Editar</button>
            <button class="list-erase" id="btn-erase-${i}" title="Apagar a tarefa">Apagar</button>
        </td>
        `;
        const corpo = document.querySelector('#lista-de-tarefas');
        corpo.appendChild(tableRoll);
    }

    function limpaInput() {
        tarefaParaAdd.value = '';
        tarefaParaAdd.focus();
    }

    function addTarefa(tarefa) {
        escreveTarefa(tarefa, tarefas.length);
        tarefas.push(tarefa);
        limpaInput();
    }

    /////////////////////////////////////////////////////////////////////////// Apaga a tarefa
    function apagarTarefa(element) {

        const botoes = element.parentElement;
        botoes.parentElement.remove();
    }

    /////////////////////////////////////////////////////////////////////////// Alternam visão dos elementos html
    function alternaLista(flag) {
        if (flag) {
            lista.style.opacity = 0;
            flagLista = false;
            lista.style.visibility = 'hidden';

        } else {
            lista.style.opacity = 1;
            flagLista = true;
            lista.style.visibility = 'visible';
        }
    }

    function alternaEdit(flag) {
        if (flag) {
            edit.style.opacity = 0;
            edit.style.visibility = 'hidden';
            flagEdit = false;
        } else {
            edit.style.opacity = 1;
            edit.style.visibility = 'visible';
            flagEdit = true;
        }
    }

    ///////////////////////////////////////////////////////////////////////////  Variáveis e eventos

    const lista = document.querySelector('#list');
    const edit = document.querySelector('#edit');
    const tarefaParaAdd = document.querySelector('#task-to-add');
    const editLista = document.querySelector('.list-edit');

    let flagLista = true;
    let flagEdit = false;
    let tarefas = [];

    tarefaParaAdd.addEventListener('keypress', function (e) {  // Quando 'enter' for pressionado na adição da tarefa
        if (e.keyCode === 13) {
            if (!tarefaParaAdd.value) return;
            addTarefa(tarefaParaAdd.value);
        }
    });

    document.addEventListener('click', function (event) {
        const element = event.target;

        if (element.classList.contains('add-tarefa')) {  // Adição de tarefa
            if (!tarefaParaAdd.value) return;
            addTarefa(tarefaParaAdd.value);
        }
        if (element.classList.contains('list-alt')) {  // Alternar visão da lista
            alternaLista(flagLista);
        }
        if (element.classList.contains('list-edit')) {  // Edição da tarefa
            if (element.id === 'btn-edit-x') return;  //  Nada acontece com a tarefa X
            alternaEdit(flagEdit);
        }
        if (element.classList.contains('list-erase')) {  // Apagar tarefa
            if (flagEdit === true) alternaEdit(flagEdit);
            if (element.id === 'btn-erase-x') return;  //  Nada acontece com a tarefa X
            apagarTarefa(element);
        }
    });
}
escopo();
