# 📝 Task Manager en Python con Docker

Este proyecto es una aplicación simple de línea de comandos para gestionar tareas. Puedes agregar, completar, eliminar y ver tareas. Las tareas se almacenan en un archivo `tasks.json`.

---

## 🐍 Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado y funcionando correctamente.
- Código fuente con:
  - `main.py` (proporcionado)
  - `Dockerfile` (ver más abajo)

---

## ⚙️ Configuración del proyecto

### 📁 Estructura de carpetas esperada

```
task-manager/
├── main.py
└── Dockerfile
```

---

## 🐳 Dockerfile usado

```Dockerfile
# Imagen base de Python ligera
FROM python:3.13.3-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo Python al contenedor
COPY main.py /app/

# Ejecuta la aplicación
CMD ["python", "main.py"]
```

---

## 🚀 Cómo ejecutar

### 🔧 Paso 1: Construir la imagen

Desde la terminal, en la carpeta donde está tu Dockerfile, ejecuta:

```bash
docker build -t task-manager .
```

---

### ▶️ Paso 2: Ejecutar la app con persistencia

Esto asegurará que el archivo `tasks.json` se guarde en tu computador:

#### En Windows (PowerShell):

```bash
docker run -it -v ${PWD}:/app task-manager
```

#### En Mac o Linux:

```bash
docker run -it -v $(pwd):/app task-manager
```

> Esto montará la carpeta local al contenedor y permitirá guardar el archivo `tasks.json` de manera persistente.

---

### ❗ Notas importantes

- El archivo `tasks.json` se guarda en la misma carpeta donde estás ejecutando el contenedor.
- Si **no montas el volumen** (`-v`), el archivo se perderá al cerrar el contenedor.
- Usa `CTRL + C` o selecciona la opción 5 para salir del programa.

---

## 📦 Compartir la imagen con otra persona

### Exportar:

```bash
docker save -o task-manager.tar task-manager
```

### Importar en otro equipo:

```bash
docker load -i task-manager.tar
```

Y luego ejecuta con:

```bash
docker run -it -v $(pwd):/app task-manager
```

---

## 📚 Créditos

- Desarrollado en el contexto del curso **TICS317 - Arquitectura de Sistemas**.
- Basado en Python 3.13 y Docker.

---
