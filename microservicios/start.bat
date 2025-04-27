@echo off
title Microservice Task Manager - Start All

echo Iniciando Storage Service...
start cmd /k "cd services\storage_service && python app.py"

echo Iniciando Logging Service...
start cmd /k "cd services\loggin_service && python app.py"

echo Iniciando Task Service...
start cmd /k "cd services\task_service && python app.py"

echo Iniciando Client (interfaz web)...
start cmd /k "cd client && python app.py"

echo Todos los servicios han sido lanzados.
pause
