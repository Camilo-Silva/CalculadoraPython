# modules/resta.py
# Módulo para operaciones de resta

def restar(a, b):
    """
    Realiza la resta de dos números.
    
    Args:
        a (float): Primer número (minuendo)
        b (float): Segundo número (sustraendo)
    
    Returns:
        float: Resultado de la resta
    """
    return a - b

def restar_lista(numeros):
    """
    Realiza la resta secuencial de una lista de números.
    
    Args:
        numeros (list): Lista de números a restar secuencialmente
    
    Returns:
        float: Resultado de la resta secuencial
    """
    if not numeros:
        return 0
    
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado -= numero
    
    return resultado
