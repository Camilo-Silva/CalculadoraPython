# modules/multiplicacion.py
# Módulo para operaciones de multiplicación

def multiplicar(a, b):
    """
    Realiza la multiplicación de dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        float: Resultado de la multiplicación
    """
    return a * b

def multiplicar_lista(numeros):
    """
    Realiza la multiplicación de una lista de números.
    
    Args:
        numeros (list): Lista de números a multiplicar
    
    Returns:
        float: Resultado de la multiplicación total
    """
    if not numeros:
        return 0
    
    resultado = 1
    for numero in numeros:
        resultado *= numero
    
    return resultado

def potencia(base, exponente):
    """
    Calcula la potencia de un número.
    
    Args:
        base (float): Número base
        exponente (float): Exponente
    
    Returns:
        float: Resultado de la potencia
    """
    return base ** exponente
