@echo off
title Sistema de Detección de Fallas - Balanceador y Servidores

echo Iniciando el sistema...

REM Abrir Servidor 1
start cmd /k "python app.py 5001"

REM Esperar 1 segundo
ping -n 2 127.0.0.1 > nul

REM Abrir Servidor 2
start cmd /k "python app.py 5002"

REM Esperar 1 segundo
ping -n 2 127.0.0.1 > nul

REM Abrir Balanceador
start cmd /k "python load_balancer.py"

REM Esperar 1 segundo
ping -n 2 127.0.0.1 > nul

REM Abrir Pruebas de errores
start cmd /k "python test_errors.py"

echo Todo listo. Revisa los navegadores o terminales para ver el sistema en acción.
pause
