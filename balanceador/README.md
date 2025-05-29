# 🧠 Sistema de Gestión de Tareas con Balanceador de Carga

Este proyecto es un sistema distribuido hecho en Python con Flask, que permite gestionar tareas de forma sencilla a través de múltiples servidores. Utiliza un **balanceador de carga** para distribuir las solicitudes entre distintas instancias del servidor.

---

## ⚙️ ¿Qué hace este proyecto?

- Permite **agregar, completar y eliminar tareas** desde una interfaz web.
- Utiliza dos servidores (`app.py`) que comparten un archivo `tasks.json` para almacenar datos.
- Un archivo `load_balancer.py` actúa como **balanceador de carga** que reparte las solicitudes entre los servidores disponibles.
- Incluye una ruta `/status` que muestra el **estado actual de los servidores** (activo/inactivo), con colores rojo o verde según su disponibilidad.

---

## 🧭 ¿Cómo funciona el balanceador?

- Entrar al puerto `localhost:8080`
- Mantiene una lista de servidores (por defecto `localhost:5001` y `localhost:5002`).
- Antes de reenviar una solicitud, verifica qué servidores están activos.
- Redirige la solicitud de forma **aleatoria** a uno de los servidores activos.
- Si un servidor está caído, lo **omite automáticamente**.
- Muestra el estado de cada servidor en `http://localhost:8080/status`, con borde y texto verde (activo) o rojo (inactivo).

---

## ▶️ ¿Cómo ejecutarlo?

### 1. Instalar dependencias

Asegúrate de tener Python 3. Luego instala las bibliotecas necesarias:

```bash
pip install flask requests
```

---

### 2. Archivos del proyecto

- **app.py**: Servidor que gestiona las tareas. Se debe ejecutar en múltiples puertos (por ejemplo, 5001 y 5002) para simular instancias paralelas.
- **load_balancer.py**: Balanceador de carga que distribuye las solicitudes entre los servidores activos.
- **index.html**: Interfaz de usuario web. Se encuentra dentro de la carpeta `templates/` y permite agregar, completar y eliminar tareas.
- **tasks.json**: Archivo donde se almacenan las tareas. Es compartido entre todos los servidores y se genera automáticamente cuando el sistema se inicia.
- **run_servers.bat**: Script para Windows que ejecuta automáticamente los dos servidores (`app.py`) y el balanceador (`load_balancer.py`) en tres terminales diferentes.

---

### 3. Estructura recomendada del proyecto

```
proyecto/
│
├── app.py
├── load_balancer.py
├── run_servers.bat
├── tasks.json         ← Se genera automáticamente
└── templates/
    └── index.html
```

---

### 4. Ejecutar manualmente

Abre **tres terminales**:

**Terminal 1** – Iniciar servidor en puerto 5001:
```bash
python app.py 5001
```

**Terminal 2** – Iniciar servidor en puerto 5002:
```bash
python app.py 5002
```

**Terminal 3** – Iniciar el balanceador de carga:
```bash
python load_balancer.py
```

---

### 5. Acceder al sistema

- Aplicación principal: [http://localhost:8080](http://localhost:8080)
- Estado de los servidores: [http://localhost:8080/status](http://localhost:8080/status)
- Acceso directo a los servidores:
  - [http://localhost:5001](http://localhost:5001)
  - [http://localhost:5002](http://localhost:5002)

---

### 6. ¿Qué es el archivo `run_servers.bat`?

Es un script para sistemas Windows que permite iniciar automáticamente:

- El servidor `app.py` en el puerto 5001.
- Otro servidor `app.py` en el puerto 5002.
- El `load_balancer.py` en el puerto 8080.

#### Para usarlo:

1. Haz doble clic en `run_servers.bat`.
2. Se abrirán tres ventanas de terminal, una para cada componente.
3. Luego accede desde tu navegador a [http://localhost:8080](http://localhost:8080).

---

## 🧪 Pruebas sugeridas

- Ingresa a `http://localhost:8080` y agrega varias tareas.
- Detén uno de los servidores (`Ctrl+C`) y observa cómo el balanceador sigue funcionando.
- Entra a `http://localhost:8080/status` para visualizar en color verde o rojo el estado de cada servidor.
- Reinicia el servidor detenido y verifica cómo vuelve a atender peticiones automáticamente.

---
