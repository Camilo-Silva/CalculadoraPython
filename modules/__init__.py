# modules/__init__.py
# Archivo de inicialización del paquete modules

# Importar todas las funciones de los módulos
from .suma import sumar, sumar_lista
from .resta import restar, restar_lista
from .multiplicacion import multiplicar, multiplicar_lista, potencia
from .division import dividir, division_entera, modulo
from .avanzadas import (
    raiz_cuadrada, raiz_n, logaritmo, factorial,
    seno, coseno, tangente
)
from .interfaz import Calculadora

# Importar interfaz gráfica solo si tkinter está disponible
try:
    from .interfaz_grafica import CalculadoraGUI
    _GUI_AVAILABLE = True
except ImportError:
    _GUI_AVAILABLE = False
    CalculadoraGUI = None

__all__ = [
    # Operaciones básicas
    'sumar', 'sumar_lista',
    'restar', 'restar_lista',
    'multiplicar', 'multiplicar_lista', 'potencia',
    'dividir', 'division_entera', 'modulo',
    # Operaciones avanzadas
    'raiz_cuadrada', 'raiz_n', 'logaritmo', 'factorial',
    'seno', 'coseno', 'tangente',
    # Interfaces
    'Calculadora'
]

# Agregar CalculadoraGUI solo si está disponible
if _GUI_AVAILABLE:
    __all__.append('CalculadoraGUI')
