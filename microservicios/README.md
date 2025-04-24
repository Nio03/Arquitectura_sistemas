# 🧠 Microservice Task Manager

Microservice Task Manager es una aplicación de arquitectura basada en microservicios desarrollada en Python con Flask. Permite gestionar tareas (crear, listar, completar y eliminar) mediante servicios independientes que se comunican entre sí vía HTTP.

---

## 🚀 Servicios y Puertos

| Servicio            | Descripción                            | Puerto | Ruta Principal                                       |
|---------------------|----------------------------------------|--------|-----------------------------------------------------|
| Client              | Interfaz de usuario web                | 5000   | http://localhost:5000                               |
| Task Service        | Lógica de negocio para tareas          | 5001   | http://localhost:5001/tasks                         |
| Storage Service     | Almacenamiento en `tasks.json`         | 5002   | http://localhost:5002/storage/tasks                |
| Logging Service     | Registro de eventos (`log.txt`)        | 5003   | http://localhost:5003/logs                         |

---

## ✅ Funcionalidades

- 📋 Crear tareas
- 📄 Ver tareas
- ✅ Marcar tareas como completadas
- 🗑️ Eliminar tareas
- 🧾 Registrar eventos en log.txt
- 💾 Guardar todas las tareas en un archivo JSON persistente

---

## 📦 Requisitos

- Python 3.7 o superior
- Pip

### 📚 Librerías necesarias

Instálalas desde tu terminal con:

```bash
pip install flask requests
# Arquitectura_sistemas