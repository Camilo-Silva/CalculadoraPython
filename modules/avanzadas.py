# modules/avanzadas.py
# Módulo para operaciones matemáticas avanzadas

import math

def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.
    
    Args:
        numero (float): Número del cual calcular la raíz cuadrada
    
    Returns:
        float: Raíz cuadrada del número
    
    Raises:
        ValueError: Si el número es negativo
    """
    if numero < 0:
        raise ValueError("Error: No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(numero)

def raiz_n(numero, n):
    """
    Calcula la raíz n-ésima de un número.
    
    Args:
        numero (float): Número del cual calcular la raíz
        n (float): Índice de la raíz
    
    Returns:
        float: Raíz n-ésima del número
    """
    return numero ** (1/n)

def logaritmo(numero, base=math.e):
    """
    Calcula el logaritmo de un número en una base específica.
    
    Args:
        numero (float): Número del cual calcular el logaritmo
        base (float): Base del logaritmo (por defecto e)
    
    Returns:
        float: Logaritmo del número en la base especificada
    
    Raises:
        ValueError: Si el número es menor o igual a cero
    """
    if numero <= 0:
        raise ValueError("Error: El logaritmo no está definido para números menores o iguales a cero")
    if base == math.e:
        return math.log(numero)
    else:
        return math.log(numero, base)

def factorial(n):
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): Número del cual calcular el factorial
    
    Returns:
        int: Factorial del número
    
    Raises:
        ValueError: Si el número es negativo o no es entero
    """
    if n < 0:
        raise ValueError("Error: El factorial no está definido para números negativos")
    if not isinstance(n, int):
        raise ValueError("Error: El factorial solo está definido para números enteros")
    return math.factorial(n)

def seno(angulo, en_radianes=True):
    """
    Calcula el seno de un ángulo.
    
    Args:
        angulo (float): Ángulo
        en_radianes (bool): True si el ángulo está en radianes, False si está en grados
    
    Returns:
        float: Seno del ángulo
    """
    if not en_radianes:
        angulo = math.radians(angulo)
    return math.sin(angulo)

def coseno(angulo, en_radianes=True):
    """
    Calcula el coseno de un ángulo.
    
    Args:
        angulo (float): Ángulo
        en_radianes (bool): True si el ángulo está en radianes, False si está en grados
    
    Returns:
        float: Coseno del ángulo
    """
    if not en_radianes:
        angulo = math.radians(angulo)
    return math.cos(angulo)

def tangente(angulo, en_radianes=True):
    """
    Calcula la tangente de un ángulo.
    
    Args:
        angulo (float): Ángulo
        en_radianes (bool): True si el ángulo está en radianes, False si está en grados
    
    Returns:
        float: Tangente del ángulo
    """
    if not en_radianes:
        angulo = math.radians(angulo)
    return math.tan(angulo)
