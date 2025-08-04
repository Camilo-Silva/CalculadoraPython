@echo off
REM Script para ejecutar la aplicación Flask en Windows

echo Instalando dependencias...
pip install -r requirements.txt

echo Ejecutando la aplicación web...
python app.py

pause
