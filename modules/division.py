# modules/division.py
# Módulo para operaciones de división

def dividir(a, b):
    """
    Realiza la división de dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        float: Resultado de la división
    
    Raises:
        ValueError: Si el divisor es cero
    """
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a / b

def division_entera(a, b):
    """
    Realiza la división entera de dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        int: Resultado de la división entera
    
    Raises:
        ValueError: Si el divisor es cero
    """
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a // b

def modulo(a, b):
    """
    Calcula el módulo (resto) de la división de dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        float: Resto de la división
    
    Raises:
        ValueError: Si el divisor es cero
    """
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a % b
