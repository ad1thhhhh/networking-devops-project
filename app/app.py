from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "driftwood_secret_key"

# Hardcoded users
users = {
    "curator": {"password": "curator123", "role": "curator"},
    "artisan": {"password": "artisan123", "role": "artisan"}
}

# In-memory task list
tasks = []


@app.route("/")
def home():
    if "username" in session:
        if session["role"] == "curator":
            return redirect("/curator")
        else:
            return redirect("/artisan")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["username"] = username
            session["role"] = users[username]["role"]
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/curator", methods=["GET", "POST"])
def curator_dashboard():
    if "username" not in session or session["role"] != "curator":
        return redirect("/login")

    if request.method == "POST":
        task_title = request.form["task"]
        tasks.append({
            "title": task_title,
            "completed": False
        })

    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / len(tasks) * 100) if tasks else 0

    return render_template("curator.html", tasks=tasks, progress=progress)


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if "username" not in session or session["role"] != "artisan":
        return redirect("/login")

    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True

    return redirect("/artisan")


@app.route("/artisan")
def artisan_dashboard():
    if "username" not in session or session["role"] != "artisan":
        return redirect("/login")

    return render_template("artisan.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
