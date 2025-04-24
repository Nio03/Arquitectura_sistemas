from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
FILE_PATH = "tasks.json"

@app.route("/")
def index():
    return "Storage Service Online"

@app.route("/storage/tasks", methods=["GET"])
def get_tasks():
    if not os.path.exists(FILE_PATH):
        return jsonify([])
    with open(FILE_PATH, "r") as f:
        return jsonify(json.load(f))

@app.route("/storage/tasks", methods=["POST"])
def save_tasks():
    tasks = request.json
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f)
    return {"status": "saved"}, 200

if __name__ == "__main__":
    app.run(port=5002)
