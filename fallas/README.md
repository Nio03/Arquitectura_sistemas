# 🛠️ Sistema de Detección de Fallas con Balanceador de Carga en Flask

Este proyecto implementa un sistema distribuido que permite:

- Gestionar tareas mediante una API REST.
- Detectar y registrar errores HTTP (`400`, `404`, `500`).
- Distribuir las solicitudes entre varios servidores Flask usando un balanceador de carga.
- Consultar estadísticas de errores en tiempo real.

---

## 🔧 Tecnologías Utilizadas

- Python 3
- Flask
- Requests
- JSON
- Script `.bat` para automatización

---

## 🧩 Arquitectura del Sistema

```
Cliente o test_errors.py
   ↓
load_balancer.py (puerto 8080)
   ↓
app.py (dos instancias: puertos 5001 y 5002)
   ↓
tasks.json (almacenamiento)
   ↓
balancer.log (registro)
```

- **5001 y 5002:** Servidores Flask que ejecutan la lógica de tareas y errores.
- **8080:** Balanceador de carga que reparte solicitudes y verifica qué servidores están activos.
- **test_errors.py:** Script que simula errores para probar el sistema.

---

## ▶️ ¿Cómo ejecutar el proyecto?

### 1. Instalar dependencias

```bash
pip install flask requests
```

### 2. Usar el script `iniciar_sistema.bat`

Para iniciar automáticamente los servidores y el balanceador:

- Haz doble clic en `iniciar_sistema.bat`
- Se abrirán 4 terminales automáticamente:
  - Servidor Flask en puerto 5001
  - Servidor Flask en puerto 5002
  - Balanceador en puerto 8080
  - Script `test_errors.py` (que genera errores y consulta estadísticas)

---

## 🧪 Resultados Esperados

### 📋 Salida del script `test_errors.py`:

```
[ERROR 400] Enviando JSON vacío...
Status: 400 | Respuesta: JSON vacío o malformado

[ERROR 404] Solicitando tarea inexistente...
Status: 404 | Respuesta: Tarea no encontrada

[ERROR 500] Forzando error interno (división por cero)...
Status: 500 | Respuesta: Error interno del servidor

[STATS] Consultando estadísticas de errores...
{
  "total_errors": 3,
  "error_types": {
    "400_BAD_REQUEST": 1,
    "404_NOT_FOUND": 1,
    "500_INTERNAL_ERROR": 1
  },
  "recent_errors": [...]
}
```

### 🌐 Puedes consultar los errores manualmente desde el navegador:

- `http://localhost:8080/errors/stats` → Ver estadísticas de errores
- `http://localhost:8080/status` → Ver qué servidores están activos
- `http://localhost:8080/health` → Verifica si el balanceador está funcionando

---

## 📁 Estructura del Proyecto

```
.
├── app.py                # Servidor Flask
├── load_balancer.py      # Balanceador de carga
├── test_errors.py        # Simula errores
├── tasks.json            # Almacena tareas
├── balancer.log          # Logs del balanceador
├── iniciar_sistema.bat   # Lanza todo el sistema automáticamente
├── README.md             # Este documento
└── templates/            # (Opcional) HTMLs si usas interfaz visual
```

---

## ✅ Beneficios

- Pruebas automatizadas de errores comunes
- Alta disponibilidad mediante balanceador
- Observabilidad con logs y estadísticas
- Listo para escalar y aplicar monitoreo más avanzado

---

> ¡Listo para ser usado en proyectos reales, demostraciones o como base para un sistema más complejo!
