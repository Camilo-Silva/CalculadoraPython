# Calculadora Profesional en Python 🧮

Una calculadora completa y profesional desarrollada en Python con **doble interfaz**: texto y gráfica, estructura modular, y tests unitarios completos.

## ✨ Características

- **Doble Interfaz**: 
  - 🖥️ **Interfaz de texto** (consola) - completa e interactiva
  - 🎨 **Interfaz gráfica** (tkinter) - moderna y fácil de usar
- **Operaciones básicas**: Suma, resta, multiplicación, división
- **Operaciones avanzadas**: Potencias, raíces, logaritmos, factorial
- **Funciones trigonométricas**: Seno, coseno, tangente (en grados y radianes)
- **Historial completo**: Guarda las operaciones realizadas
- **Atajos de teclado**: Soporte completo para uso con teclado en la GUI
- **Tests unitarios**: Cobertura completa de todas las funciones
- **Estructura modular**: Cada función en su propio archivo para fácil mantenimiento

## 📁 Estructura del Proyecto

```
CALCULADORA/
│   main.py                 # Archivo principal (selector de interfaz)
│   main_gui.py            # Ejecutar directamente la interfaz gráfica
│   demo.py                # Demostración de todas las funciones
│   README.md              # Documentación del proyecto
│   requirements.txt       # Dependencias (ninguna externa requerida)
│
├── modules/               # Módulos de funciones matemáticas
│   │   __init__.py       # Inicialización del paquete
│   │   suma.py           # Funciones de suma
│   │   resta.py          # Funciones de resta
│   │   multiplicacion.py # Funciones de multiplicación y potencias
│   │   division.py       # Funciones de división
│   │   avanzadas.py      # Funciones matemáticas avanzadas
│   │   interfaz.py       # Interfaz de texto (consola)
│   └   interfaz_grafica.py # Interfaz gráfica (tkinter)
│
└── tests/                # Tests unitarios
    │   __init__.py       # Inicialización del paquete de tests
    │   run_all_tests.py  # Script para ejecutar todos los tests
    │   test_suma.py      # Tests para funciones de suma
    │   test_resta.py     # Tests para funciones de resta
    │   test_multiplicacion.py # Tests para funciones de multiplicación
    │   test_division.py  # Tests para funciones de división
    │   test_avanzadas.py # Tests para funciones avanzadas
    └   test_interfaz_grafica.py # Tests para la interfaz gráfica
```

## 🚀 Cómo usar

### Instalación y ejecución

1. **Clona o descarga el proyecto**
2. **Navega al directorio del proyecto**:
   ```powershell
   cd C:\Users\csilva\Desktop\CALCULADORA
   ```

### Opciones de ejecución

#### **Opción 1: Selector de interfaz (Recomendado)**
```powershell
python main.py
```
Te permite elegir entre interfaz de texto o gráfica.

#### **Opción 2: Interfaz gráfica directa**
```powershell
python main_gui.py
```
Ejecuta directamente la interfaz gráfica moderna.

#### **Opción 3: Ver demostración**
```powershell
python demo.py
```
Muestra todas las funciones disponibles sin interfaz.

### 🎨 Interfaz Gráfica

La interfaz gráfica incluye:

- **Display grande** con números claramente visibles
- **Botones organizados** por tipo de operación con colores distintivos
- **Funciones científicas** en pestañas organizadas
- **Historial completo** con scroll y opciones de copiado
- **Configuración de ángulos** (grados/radianes) para funciones trigonométricas
- **Atajos de teclado** completos:
  - Números y operadores directos
  - `Enter` o `=` para calcular
  - `C` o `Delete` para limpiar
  - `Backspace` para borrar último dígito
  - `Esc` para limpiar entrada actual

### 🖥️ Interfaz de Texto

La interfaz de consola ofrece:

- **Menú interactivo** con todas las operaciones
- **Manejo robusto de errores** con mensajes claros
- **Historial de operaciones** (últimas 20)
- **Soporte completo** para todas las funciones matemáticas

### Ejemplo de uso - Interfaz de Texto

```
================================
    CALCULADORA PROFESIONAL
================================
1.  Suma
2.  Resta
3.  Multiplicación
4.  División
5.  Potencia
6.  Raíz cuadrada
7.  Logaritmo
8.  Factorial
9.  Funciones trigonométricas
10. Ver historial
11. Limpiar historial
0.  Salir
================================
```

### Ejemplo de uso - Interfaz Gráfica

La interfaz gráfica presenta una calculadora moderna con:
- Display principal en la parte superior
- Botones numéricos organizados como una calculadora tradicional
- Botones de operaciones con colores distintivos
- Pestañas para funciones científicas y configuración
- Área de historial en la parte inferior

## 🧪 Ejecutar Tests

Para ejecutar todos los tests:

```powershell
python tests\run_all_tests.py
```

Para ejecutar tests individuales:

```powershell
python -m unittest tests.test_suma
python -m unittest tests.test_division
# etc.
```

## 📚 Funciones Disponibles

### Operaciones Básicas
- `sumar(a, b)`: Suma de dos números
- `restar(a, b)`: Resta de dos números
- `multiplicar(a, b)`: Multiplicación de dos números
- `dividir(a, b)`: División de dos números
- `potencia(base, exponente)`: Cálculo de potencias

### Operaciones Avanzadas
- `raiz_cuadrada(numero)`: Raíz cuadrada
- `raiz_n(numero, n)`: Raíz n-ésima
- `logaritmo(numero, base)`: Logaritmo en cualquier base
- `factorial(n)`: Factorial de un número entero
- `seno(angulo, en_radianes)`: Función seno
- `coseno(angulo, en_radianes)`: Función coseno
- `tangente(angulo, en_radianes)`: Función tangente

### Operaciones con Listas
- `sumar_lista(numeros)`: Suma todos los números de una lista
- `multiplicar_lista(numeros)`: Multiplica todos los números de una lista
- `restar_lista(numeros)`: Resta secuencial de una lista

## 🛠️ Desarrollo

### Agregar nuevas funciones

1. Crea un nuevo archivo en `modules/` para tu función
2. Implementa la función con documentación apropiada
3. Agrega la importación en `modules/__init__.py`
4. Crea tests correspondientes en `tests/`
5. Actualiza la interfaz si es necesario

### Estructura de una función

```python
def mi_funcion(parametro):
    """
    Descripción de la función.
    
    Args:
        parametro (tipo): Descripción del parámetro
    
    Returns:
        tipo: Descripción del retorno
    
    Raises:
        ErrorTipo: Descripción del error
    """
    # Implementación
    return resultado
```

## 🔧 Requisitos

- **Python 3.6+**
- **Bibliotecas estándar**: math, sys, unittest, tkinter
- **tkinter** (incluido con Python en Windows, instalación estándar)
- **No se requieren dependencias externas**

> **Nota**: Si tkinter no está disponible en tu sistema, la calculadora funcionará perfectamente con la interfaz de texto.

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Mantén la estructura modular
2. Agrega tests para todas las funciones nuevas
3. Documenta apropiadamente el código
4. Sigue las convenciones de nomenclatura de Python

## 📄 Licencia

Este proyecto está disponible bajo licencia MIT.

---

**¡Disfruta usando la calculadora profesional! 🎉**
│   README.md
│
├───modules
│       suma.py
│       resta.py
│       ...
│
└───tests
        test_suma.py
        test_resta.py
        ...
```
