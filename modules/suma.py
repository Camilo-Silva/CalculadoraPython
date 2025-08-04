# modules/suma.py
# Módulo para operaciones de suma

def sumar(a, b):
    """
    Realiza la suma de dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
    
    Returns:
        float: Resultado de la suma
    """
    return a + b

def sumar_lista(numeros):
    """
    Realiza la suma de una lista de números.
    
    Args:
        numeros (list): Lista de números a sumar
    
    Returns:
        float: Resultado de la suma total
    """
    return sum(numeros)
