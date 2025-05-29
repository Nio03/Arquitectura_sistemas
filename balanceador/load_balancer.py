from flask import Flask, request, Response
import requests
import random

app = Flask(__name__)

# Lista de servidores disponibles
ALL_SERVERS = ['http://localhost:5001', 'http://localhost:5002']

# Verifica cuáles servidores están activos
def get_active_servers():
    active = []
    for server in ALL_SERVERS:
        try:
            requests.get(server, timeout=0.5)
            active.append(server)
        except requests.exceptions.RequestException:
            pass
    return active

# Página de estado HTML con diseño bonito
@app.route('/status')
def status():
    estados = {}
    for server in ALL_SERVERS:
        try:
            requests.get(server, timeout=1)
            estados[server] = "✅ ACTIVO"
        except requests.exceptions.RequestException:
            estados[server] = "❌ INACTIVO"

    html = """
    <html>
    <head>
        <title>Estado de los Servidores</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }
            h2 {
                color: #333;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: white;
                margin: 10px 0;
                padding: 15px;
                border-left: 10px solid;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-size: 18px;
            }
            .activo {
                border-color: #4CAF50;
                color: #4CAF50;
            }
            .inactivo {
                border-color: #F44336;
                color: #F44336;
            }
        </style>
    </head>
    <body>
        <h2>🔍 Estado de los Servidores</h2>
        <ul>
    """

    for srv, estado in estados.items():
        clase = "activo" if "ACTIVO" in estado else "inactivo"
        # Aplica color rojo si es inactivo
        style = ' style="color: #F44336;"' if "INACTIVO" in estado else ""
        html += f'<li class="{clase}">{srv}<span{style}>{estado}</span></li>'


    html += """
        </ul>
    </body>
    </html>
    """
    return html

# Ruta general que redirige la solicitud a un servidor activo
@app.route('/', defaults={'path': ''}, methods=["GET", "POST"])
@app.route('/<path:path>', methods=["GET", "POST"])
def proxy(path):
    if path == "status":
        return status()

    active_servers = get_active_servers()
    if not active_servers:
        return Response("❌ Ningún servidor disponible", status=503)

    server = random.choice(active_servers)
    url = f"{server}/{path}"

    try:
        if request.method == "POST":
            resp = requests.post(url, data=request.form)
        else:
            resp = requests.get(url, params=request.args)
    except requests.exceptions.RequestException:
        return Response("❌ Error al contactar al servidor", status=503)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers)

if __name__ == "__main__":
    app.run(port=8080)




