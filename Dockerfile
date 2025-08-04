# Dockerfile para la Calculadora Web
FROM python:3.11-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8080

# Configurar variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=8080

# Comando para ejecutar la aplicación Flask (NO main.py)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
