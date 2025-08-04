# Calculadora Web 🧮

Una calculadora web moderna y funcional desarrollada con Python Flask que incluye:

## Características ✨

- **Calculadora Básica**: Operaciones aritméticas fundamentales
- **Calculadora Científica**: Funciones matemáticas avanzadas
- **Operaciones con Listas**: Cálculos con múltiples números
- **Interfaz Moderna**: Diseño responsivo y atractivo
- **Historial**: Registro de todos los cálculos realizados
- **Soporte de Teclado**: Navega usando el teclado

## Funcionalidades 🚀

### Calculadora Básica
- ➕ Suma, ➖ Resta, ✖️ Multiplicación, ➗ División
- 🔢 División entera, 📐 Módulo, 🔺 Potencia

### Calculadora Científica
- 🔍 Raíz cuadrada y raíz n-ésima
- 📊 Logaritmos (natural y base 10)
- 📈 Funciones trigonométricas (sin, cos, tan)
- ❗ Factorial

### Operaciones con Listas
- 📝 Agregar múltiples números
- 🧮 Suma, resta y multiplicación de listas
- 🗑️ Gestión dinámica de números

## Instalación y Ejecución 📦

### Requisitos
- Python 3.11+
- Flask 2.3+

### Instalación Local

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```
   O usar el script:
   - Windows: `run_web.bat`
   - Linux/Mac: `run_web.sh`

3. **Abrir en el navegador**:
   ```
   http://localhost:5000
   ```

## Deployment en la Nube ☁️

### Heroku
1. Crear una aplicación en Heroku
2. Conectar el repositorio
3. Los archivos `Procfile` y `runtime.txt` están configurados

### Render
1. Crear un servicio web en Render
2. Conectar el repositorio
3. El archivo `render.yaml` está configurado

### PythonAnywhere
1. Subir los archivos al servidor
2. Configurar una aplicación web Flask
3. Especificar `app.py` como archivo principal

## Estructura del Proyecto 📁

```
calculadora-web/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias
├── Procfile              # Configuración Heroku
├── runtime.txt           # Versión Python para Heroku
├── render.yaml           # Configuración Render
├── templates/
│   └── index.html        # Plantilla HTML principal
├── static/
│   ├── css/
│   │   └── style.css     # Estilos CSS
│   └── js/
│       └── calculator.js # Lógica JavaScript
└── modules/              # Módulos matemáticos existentes
    ├── suma.py
    ├── resta.py
    ├── multiplicacion.py
    ├── division.py
    └── avanzadas.py
```

## API Endpoints 🔌

### POST `/api/calculate`
Realiza cálculos matemáticos

**Operaciones Básicas**:
```json
{
  "operation": "basic",
  "num1": 10,
  "num2": 5,
  "operator": "+"
}
```

**Operaciones Avanzadas**:
```json
{
  "operation": "advanced",
  "function": "sqrt",
  "number": 16
}
```

**Operaciones con Listas**:
```json
{
  "operation": "list",
  "numbers": [1, 2, 3, 4],
  "operator": "sum"
}
```

## Tecnologías Utilizadas 🛠️

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilos**: CSS Grid, Flexbox, Gradientes
- **Iconos**: Font Awesome
- **Fuentes**: Google Fonts (Poppins)

## Características Técnicas 🔧

- **Responsive Design**: Funciona en dispositivos móviles y desktop
- **API REST**: Comunicación asíncrona con el backend
- **Manejo de Errores**: Validación y mensajes informativos
- **Accesibilidad**: Soporte completo de teclado
- **Optimizado**: Código limpio y modular

## Autor 👨‍💻

Desarrollado usando los módulos matemáticos existentes del proyecto Calculadora Python.

## Licencia 📄

Este proyecto mantiene la licencia del proyecto original.
