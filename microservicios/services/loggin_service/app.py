from flask import Flask, request, jsonify
import os

app = Flask(__name__)
LOG_FILE = "log.txt"

@app.route("/")
def index():
    return "Logging Service Online"

@app.route("/log", methods=["POST"])
def log_event():
    data = request.json
    message = data.get("message", "Sin mensaje")
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    return {"status": "ok"}, 200

@app.route("/logs", methods=["GET"])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify([])
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    return jsonify([line.strip() for line in lines])

if __name__ == "__main__":
    app.run(port=5003)
