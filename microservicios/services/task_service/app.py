from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
STORAGE_API = "http://localhost:5002/storage/tasks"
LOGGING_API = "http://localhost:5003/log"

def get_tasks():
    return requests.get(STORAGE_API).json()

def save_tasks(tasks):
    requests.post(STORAGE_API, json=tasks)

def log_event(message):
    try:
        response = requests.post(LOGGING_API, json={"message": message})
        response.raise_for_status()
    except:
        pass


@app.route("/")
def index():
    return "Task Service Online"

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = get_tasks()
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    log_event(f"Tarea creada: {task['title']}")
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def complete_task(task_id):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            log_event(f"Tarea completada: {task['title']}")
    save_tasks(tasks)
    return {"status": "completed"}

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = get_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    for t in tasks:
        if t["id"] == task_id:
            log_event(f"Tarea eliminada: {t['title']}")
    save_tasks(new_tasks)
    return {"status": "deleted"}

if __name__ == "__main__":
    app.run(port=5001)
