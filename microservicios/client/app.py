from flask import Flask, request, redirect, render_template_string
import requests

app = Flask(__name__)

TASK_API = "http://localhost:5001/tasks"

TEMPLATE = """
<h1>Gestor de Tareas</h1>

<form action="/" method="post">
    <input type="text" name="title" placeholder="Nueva tarea" required>
    <button type="submit">Agregar</button>
</form>

<ul>
{% for task in tasks %}
    <li>
        {{ task['title'] }} - {% if task['completed'] %}✅{% else %}❌{% endif %}
        {% if not task['completed'] %}
            <form action="/complete/{{ task['id'] }}" method="post" style="display:inline;">
                <button type="submit">✅ Completar</button>
            </form>
        {% endif %}
        <form action="/delete/{{ task['id'] }}" method="post" style="display:inline;">
            <button type="submit">🗑️ Eliminar</button>
        </form>
    </li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        requests.post(TASK_API, json={"title": title})
        return redirect("/")
    
    tasks = requests.get(TASK_API).json()
    return render_template_string(TEMPLATE, tasks=tasks)

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    requests.put(f"http://localhost:5001/tasks/{task_id}/complete")
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    requests.delete(f"http://localhost:5001/tasks/{task_id}")
    return redirect("/")

if __name__ == "__main__":
    app.run(port=5000)
