from flask import Flask, request, jsonify
import requests
import random
import time

app = Flask(__name__)
SERVERS = ['http://localhost:5001', 'http://localhost:5002']
LOG_FILE = 'balancer.log'


def is_server_alive(url):
    try:
        response = requests.get(f'{url}/health', timeout=1)
        return response.status_code == 200
    except:
        return False


def log(message):
    with open(LOG_FILE, 'a') as f:
        f.write(f'[{time.ctime()}] {message}\n')


@app.route('/<path:path>', methods=['GET', 'POST'])
def route(path):
    alive = [s for s in SERVERS if is_server_alive(s)]
    if not alive:
        return 'No hay servidores disponibles', 503
    server = random.choice(alive)
    url = f'{server}/{path}'
    log(f'Reenviando a: {url}')

    try:
        if request.method == 'GET':
            res = requests.get(url)
        else:
            res = requests.post(url, json=request.get_json())
        return (res.content, res.status_code, res.headers.items())
    except Exception as e:
        return f'Error al reenviar: {str(e)}', 500


@app.route('/status')
def status():
    status_list = {s: is_server_alive(s) for s in SERVERS}
    return jsonify(status_list)


@app.route('/health')
def health():
    return 'Balanceador activo', 200


if __name__ == '__main__':
    app.run(port=8080)
