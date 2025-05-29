@echo off
title Sistema de Gestión de Tareas - TICS317

:: Iniciar servidor en puerto 5001
start cmd /k "python app.py 5001"

:: Iniciar servidor en puerto 5002
start cmd /k "python app.py 5002"

:: Iniciar el balanceador en puerto 8080
start cmd /k "python load_balancer.py"

echo Servidores y balanceador iniciados.
pause
