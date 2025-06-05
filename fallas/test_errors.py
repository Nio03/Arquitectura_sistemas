import requests

BASE_URL = 'http://localhost:8080'

print("------ TEST DE ERRORES ------")

# 1. Error 400: JSON vacío o malformado
print("\n[ERROR 400] Enviando JSON vacío...")
try:
    res = requests.post(f'{BASE_URL}/tasks', json={})
    print(f"Status: {res.status_code} | Respuesta: {res.text}")
except Exception as e:
    print("Error en la solicitud:", e)

# 2. Error 404: Tarea inexistente
print("\n[ERROR 404] Solicitando tarea inexistente...")
try:
    res = requests.get(f'{BASE_URL}/tasks/999')
    print(f"Status: {res.status_code} | Respuesta: {res.text}")
except Exception as e:
    print("Error en la solicitud:", e)

# 3. Error 500: Forzar división por cero
print("\n[ERROR 500] Forzando error interno (división por cero)...")
try:
    res = requests.get(f'{BASE_URL}/error500')
    print(f"Status: {res.status_code} | Respuesta: {res.text}")
except Exception as e:
    print("Error en la solicitud:", e)

# 4. Consultar estadísticas después del test
print("\n[STATS] Consultando estadísticas de errores...")
try:
    res = requests.get(f'{BASE_URL}/errors/stats')
    print("Estadísticas de errores:", res.json())
except Exception as e:
    print("Error al obtener estadísticas:", e)
