document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('task-form');
    const input = document.getElementById('task-input');
    const tasksContainer = document.getElementById('tasks-container');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const taskText = input.value
        if (taskText !== '') {
            addTask(taskText);
            input.value = '';
        }
    });

    function addTask(taskText) {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${taskText}</span>
            <div>
                <button class="delete-btn">Delete</button>
                <button class="edit-btn">Edit</button>
            </div>
        `;
        tasksContainer.appendChild(li);

        const deleteBtn = li.querySelector('.delete-btn');
        deleteBtn.addEventListener('click', function() {
            li.remove();
        });

        const editBtn = li.querySelector('.edit-btn');
        editBtn.addEventListener('click', function() {
            const span = li.querySelector('span');
            const newText = prompt('Edit task:', span.textContent);
            if (newText !== null) {
                span.textContent = newText.trim();
            }
        });
    }
});

