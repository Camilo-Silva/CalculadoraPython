# Guía de Deployment - Calculadora Web

## 🚀 Opciones de Deployment

### 1. Heroku (Recomendado)

**Pasos:**
1. Crear cuenta en [Heroku](https://heroku.com)
2. Instalar Heroku CLI
3. Crear una nueva app:
   ```bash
   heroku create nombre-de-tu-calculadora
   ```
4. Hacer push del código:
   ```bash
   git add .
   git commit -m "Deploy calculadora web"
   git push heroku main
   ```

**Archivos necesarios (ya incluidos):**
- `Procfile`: Configuración del servidor
- `runtime.txt`: Versión de Python
- `requirements.txt`: Dependencias

### 2. Render (Alternativa gratuita)

**Pasos:**
1. Crear cuenta en [Render](https://render.com)
2. Conectar tu repositorio de GitHub
3. Crear un nuevo "Web Service"
4. Configurar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

**Archivo necesario (ya incluido):**
- `render.yaml`: Configuración automática

### 3. PythonAnywhere

**Pasos:**
1. Crear cuenta en [PythonAnywhere](https://pythonanywhere.com)
2. Subir archivos via Files o Git
3. Crear una nueva Web App
4. Configurar:
   - Framework: Flask
   - Python version: 3.11
   - Source code: `/home/usuario/calculadora/`
   - WSGI file: apuntar a `app.py`

### 4. Railway

**Pasos:**
1. Crear cuenta en [Railway](https://railway.app)
2. Conectar repositorio de GitHub
3. El deployment es automático con los archivos de configuración

### 5. Google Cloud Run

**Pasos:**
1. Crear `Dockerfile`:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8080
   CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
   ```
2. Desplegar en Cloud Run

## 🔧 Configuración de Variables de Entorno

Para producción, puedes configurar:

```bash
# Heroku
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=tu-clave-secreta

# Render/Railway (en el dashboard)
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta
```

## ⚠️ Solución de Problemas Comunes

### Error: ModuleNotFoundError: No module named '_tkinter'

**Problema**: El contenedor intenta ejecutar `main.py` en lugar de `app.py`

**Solución**: 
1. Asegurar que el Dockerfile ejecute `app.py`:
   ```dockerfile
   CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
   ```
2. El archivo `modules/__init__.py` ya está configurado para manejar este error automáticamente

### Error: Application not found

**Problema**: La plataforma no encuentra la aplicación Flask

**Solución**: Verificar que:
- El archivo se llame `app.py` (no `main.py`)
- La variable Flask se llame `app`
- El `Procfile` contenga: `web: gunicorn app:app`

## 📊 Monitoreo

Una vez desplegado, puedes monitorear:

- **Logs**: `heroku logs --tail` (Heroku)
- **Métricas**: Panel de control de cada plataforma
- **Errores**: Configurar alertas en el dashboard

## 💡 Tips de Optimización

1. **Gzip**: Flask automáticamente comprime respuestas
2. **CDN**: Usar CDN para assets estáticos
3. **Caching**: Implementar Redis para cache (opcional)
4. **SSL**: Todas las plataformas incluyen HTTPS gratuito

## 🔒 Seguridad

- Todas las plataformas incluyen HTTPS automático
- Las variables de entorno están seguras
- No hay datos sensibles en el código

## 📱 Testing de Deployment

Después del deployment, probar:

1. ✅ Calculadora básica
2. ✅ Funciones científicas
3. ✅ Operaciones con listas
4. ✅ Historial
5. ✅ Responsive design en móviles

## 🌍 URLs de Ejemplo

- Heroku: `https://mi-calculadora.herokuapp.com`
- Render: `https://mi-calculadora.onrender.com`
- Railway: `https://mi-calculadora.up.railway.app`

## 📞 Soporte

Si encuentras problemas:

1. Revisar logs de la plataforma
2. Verificar que todos los archivos estén subidos
3. Comprobar que requirements.txt esté actualizado
4. Probar localmente primero: `python app.py`
