async function fetchTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    const list = document.getElementById('taskList');
    list.innerHTML = '';

    tasks.forEach(task => {
        const li = document.createElement('li');

        let text = task.task;
        if (task.status === "completed") {
            text = "<s>" + task.task + "</s>";
        }

        li.innerHTML = `
            <span>${text}</span>
            <div>
                <button onclick="toggleTask(${task.id})">✔</button>
                <button onclick="deleteTask(${task.id})">✖</button>
            </div>
        `;

        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById('taskInput');
    if (!input.value) return;

    await fetch('/tasks', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({task: input.value})
    });

    input.value = '';
    fetchTasks();
}

async function deleteTask(id) {
    await fetch('/tasks/' + id, {method: 'DELETE'});
    fetchTasks();
}

async function toggleTask(id) {
    await fetch('/tasks/' + id + '/toggle', {method: 'PUT'});
    fetchTasks();
}

fetchTasks();
