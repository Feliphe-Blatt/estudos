function escopo() {

    let lista = document.querySelector('#list');
    const edit = document.querySelector('#edit');
    let tarefaParaAdd = document.querySelector('#task-to-add');
    let editLista = document.querySelector('.list-edit');

    let flagLista = false;
    let flagEdit = false;
    
    tarefaParaAdd.addEventListener('keypress', function (e) {
        if (e.keyCode === 13) {
            if (!tarefaParaAdd.value) return;
            addTarefa(tarefaParaAdd.value);
        }
    });

    function addTarefa(tarefa) {
        const tableRoll = document.createElement('tr');
        tableRoll.innerHTML = `
        <td>
        <h1 class="listItem">
            "${tarefa}"
        </h1>
        </td>
        <td>
            <button class="list-edit">Editar</button>
            <button class="listErase">Apagar</button>
        </td>
        `;
        lista.appendChild(tableRoll);
    }

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
            editLista.innerHTML = 'Editar';
            edit.style.visibility = 'hidden';
            flagEdit = false;
        } else {
            edit.style.opacity = 1;
            editLista.innerHTML = 'Cancelar';
            edit.style.visibility = 'visible';
            flagEdit = true;
        }
    }

    document.addEventListener('click', function (event) {
        const element = event.target;
        if (element.classList.contains('add-tarefa')) {
            if (!tarefaParaAdd.value) return;
            addTarefa(tarefaParaAdd.value);
        }
        if (element.classList.contains('alternar')) {
            alternaLista(flagLista);
        }
        if (element.classList.contains('list-edit')) {
            alternaEdit(flagEdit);
        }
    });
}
escopo();
