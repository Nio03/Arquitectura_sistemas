from flask import Flask, request, jsonify, render_template
import json, os, sys

app = Flask(__name__)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks, port=PORT)

@app.route('/tasks/add', methods=['POST'])
def add_task():
    title = request.form.get("title", "")
    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    return "", 302, {'Location': '/'}

@app.route('/tasks/<int:task_id>/complete')
def complete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
    return "", 302, {'Location': '/'}

@app.route('/tasks/<int:task_id>/delete')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return "", 302, {'Location': '/'}

if __name__ == "__main__":
    app.run(port=PORT)
