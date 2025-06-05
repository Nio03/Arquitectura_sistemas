from flask import Flask, request, jsonify
import json
import sys

app = Flask(__name__)

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
TASK_FILE = 'tasks.json'
error_log = []
error_stats = {'400_BAD_REQUEST': 0, '404_NOT_FOUND': 0, '500_INTERNAL_ERROR': 0}


# Helpers
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)


# Routes
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'task' not in data:
        error_stats['400_BAD_REQUEST'] += 1
        error_log.append('400_BAD_REQUEST: JSON vacío o malformado')
        return 'JSON vacío o malformado', 400
    tasks = load_tasks()
    tasks.append(data['task'])
    save_tasks(tasks)
    return 'Tarea creada', 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = load_tasks()
    if task_id < 0 or task_id >= len(tasks):
        error_stats['404_NOT_FOUND'] += 1
        error_log.append(f'404_NOT_FOUND: Tarea {task_id} no existe')
        return 'Tarea no encontrada', 404
    return jsonify({'task': tasks[task_id]})


@app.route('/error500')
def error_500():
    try:
        1 / 0  # Fuerza un error
    except Exception as e:
        error_stats['500_INTERNAL_ERROR'] += 1
        error_log.append(f'500_INTERNAL_ERROR: {str(e)}')
        return 'Error interno del servidor', 500


@app.route('/errors/stats')
def error_stats_view():
    return jsonify({
        'total_errors': sum(error_stats.values()),
        'error_types': dict(error_stats),
        'recent_errors': error_log[-10:]
    })


@app.route('/health')
def health_check():
    return 'OK', 200


if __name__ == '__main__':
    app.run(port=PORT)
from flask import Flask, request, jsonify
import json
import sys

app = Flask(__name__)

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5001
TASK_FILE = 'tasks.json'
error_log = []
error_stats = {'400_BAD_REQUEST': 0, '404_NOT_FOUND': 0, '500_INTERNAL_ERROR': 0}


# Helpers
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)


# Routes
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'task' not in data:
        error_stats['400_BAD_REQUEST'] += 1
        error_log.append('400_BAD_REQUEST: JSON vacío o malformado')
        return 'JSON vacío o malformado', 400
    tasks = load_tasks()
    tasks.append(data['task'])
    save_tasks(tasks)
    return 'Tarea creada', 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = load_tasks()
    if task_id < 0 or task_id >= len(tasks):
        error_stats['404_NOT_FOUND'] += 1
        error_log.append(f'404_NOT_FOUND: Tarea {task_id} no existe')
        return 'Tarea no encontrada', 404
    return jsonify({'task': tasks[task_id]})


@app.route('/error500')
def error_500():
    try:
        1 / 0  # Fuerza un error
    except Exception as e:
        error_stats['500_INTERNAL_ERROR'] += 1
        error_log.append(f'500_INTERNAL_ERROR: {str(e)}')
        return 'Error interno del servidor', 500


@app.route('/errors/stats')
def error_stats_view():
    return jsonify({
        'total_errors': sum(error_stats.values()),
        'error_types': dict(error_stats),
        'recent_errors': error_log[-10:]
    })


@app.route('/health')
def health_check():
    return 'OK', 200


if __name__ == '__main__':
    app.run(port=PORT)
