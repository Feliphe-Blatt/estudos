document.addEventListener('DOMContentLoaded', function () {
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');
    const timerDisplay = document.getElementById('timerDisplay');

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    let activeTaskIndex = null;
    let timerInterval;

    function saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function displayTasks() {
        taskList.innerHTML = '';
        tasks.forEach(function (taskText, index) {
            const li = document.createElement('li');
            li.textContent = taskText;

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Excluir';
            deleteButton.addEventListener('click', function () {
                tasks.splice(index, 1);
                saveTasks();
                displayTasks();
            });

            const editButton = document.createElement('button');
            editButton.textContent = 'Editar';
            editButton.addEventListener('click', function () {
                const editedTask = prompt('Editar tarefa:', taskText);
                if (editedTask !== null) {
                    tasks[index] = editedTask;
                    saveTasks();
                    displayTasks();
                }
            });

            const startButton = document.createElement('button');
            startButton.textContent = 'Iniciar';
            startButton.addEventListener('click', function () {
                if (activeTaskIndex !== null) {
                    clearInterval(timerInterval);
                }
                activeTaskIndex = index;
                startTimer();
            });

            const stopButton = document.createElement('button');
            stopButton.textContent = 'Parar';
            stopButton.addEventListener('click', function () {
                activeTaskIndex = null;
                clearInterval(timerInterval);
                updateTimerDisplay(0);
            });

            li.appendChild(deleteButton);
            li.appendChild(editButton);
            li.appendChild(startButton);
            li.appendChild(stopButton);
            taskList.appendChild(li);
        });
    }

    function startTimer() {
        let startTime = Date.now();

        timerInterval = setInterval(function () {
            const elapsedTime = Math.floor((Date.now() - startTime) / 1000);
            updateTimerDisplay(elapsedTime);
        }, 1000);
    }

    function updateTimerDisplay(timeInSeconds) {
        const minutes = Math.floor(timeInSeconds / 60);
        const seconds = timeInSeconds % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }

    displayTasks();

    taskForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const newTask = taskInput.value;
        tasks.push(newTask);
        saveTasks();
        displayTasks();
        taskForm.reset();
    });
});
