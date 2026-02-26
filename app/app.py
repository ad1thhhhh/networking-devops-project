from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Barista Task List ☕</title>
        <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #3e2723, #795548);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .card {
            background: #fff8f2;
            padding: 40px;
            border-radius: 20px;
            width: 400px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            color: #4e342e;
        }

        input {
            padding: 12px;
            width: 70%;
            border-radius: 8px;
            border: 1px solid #ccc;
            outline: none;
        }

        button {
            padding: 10px 14px;
            background: #6d4c41;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.2s;
            margin-left: 5px;
        }

        button:hover {
            background: #5d4037;
            transform: scale(1.05);
        }

        ul {
            list-style: none;
            padding: 0;
            margin-top: 20px;
        }

        li {
            background: white;
            margin: 10px 0;
            padding: 12px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }

        s {
        color: #999;
        }
    </style>
    </head>
                <body>
            <div class="card">
                <h1>☕ Barista Task List</h1>

                <div style="margin-bottom:20px;">
                    <input type="text" id="taskInput" placeholder="Enter new barista task">
                    <button onclick="addTask()">Add</button>
                </div>

                <ul id="taskList"></ul>
            </div>

            <script>
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
                                <button onclick="deleteTask(${task.id})">❌</button>
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
            </script>
        </body>
    </html>
    """

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "task": data.get("task"),
        "status": "pending"
    }
    tasks.append(task)
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

@app.route("/tasks/<int:task_id>/toggle", methods=["PUT"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "pending":
                task["status"] = "completed"
            else:
                task["status"] = "pending"
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
