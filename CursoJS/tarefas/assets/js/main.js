function escopo() {

    const lista = document.getElementById('lista');
    const edit = document.getElementById('edit');
    const editLista = document.querySelector('.listEdit');
    const tarefaASerEditada = document.getElementById('taskToEdit');

    let flagLista = false;
    let flagEdit = false;

    function alternaLista(flag) {
        if (flag) {
            for (let i = 1; i >= 0; i--) {
                lista.style.opacity = i;
            }
            flagLista = false;

        } else {
            for (let i = 0; i <= 1; i++) {
                lista.style.opacity = i;
            }
            flagLista = true;
        }
    }

    function alternaEdit(flag) {
        if (flag) {
            for (let i = 1; i >= 0; i--) {
                edit.style.opacity = i;
            }
            flagEdit = false;
            editLista.innerHTML = 'Editar';

        } else {
            for (let i = 0; i <= 1; i++) {
                edit.style.opacity = i;
            }
            flagEdit = true;
            editLista.innerHTML = 'Cancelar';
        }
    }

    document.addEventListener('click', function (event) {
        const element = event.target;

        if (element.classList.contains('editTarefa')) {
            
        }
        if (element.classList.contains('alternar')) {
            alternaLista(flagLista);
        }
        if (element.classList.contains('listEdit')) {
            alternaEdit(flagEdit);
        }
    });
}
escopo();
