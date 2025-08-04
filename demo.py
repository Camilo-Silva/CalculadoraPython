# demo.py
# Script de demostración de las funciones de la calculadora

import sys
import os

# Agregar el directorio actual al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, logaritmo, factorial,
    seno, coseno, tangente,
    sumar_lista, multiplicar_lista
)

def demo_operaciones_basicas():
    """Demostración de operaciones básicas."""
    print("🔢 OPERACIONES BÁSICAS")
    print("=" * 40)
    
    # Suma
    resultado = sumar(15, 25)
    print(f"Suma: 15 + 25 = {resultado}")
    
    # Resta
    resultado = restar(50, 18)
    print(f"Resta: 50 - 18 = {resultado}")
    
    # Multiplicación
    resultado = multiplicar(7, 8)
    print(f"Multiplicación: 7 × 8 = {resultado}")
    
    # División
    resultado = dividir(84, 7)
    print(f"División: 84 ÷ 7 = {resultado}")
    
    # Potencia
    resultado = potencia(2, 8)
    print(f"Potencia: 2^8 = {resultado}")
    
    print()

def demo_operaciones_avanzadas():
    """Demostración de operaciones avanzadas."""
    print("🚀 OPERACIONES AVANZADAS")
    print("=" * 40)
    
    # Raíz cuadrada
    resultado = raiz_cuadrada(64)
    print(f"Raíz cuadrada: √64 = {resultado}")
    
    # Logaritmo natural
    resultado = logaritmo(2.718281828)
    print(f"Logaritmo natural: ln(e) = {resultado:.6f}")
    
    # Logaritmo base 10
    resultado = logaritmo(1000, 10)
    print(f"Logaritmo base 10: log₁₀(1000) = {resultado}")
    
    # Factorial
    resultado = factorial(6)
    print(f"Factorial: 6! = {resultado}")
    
    print()

def demo_funciones_trigonometricas():
    """Demostración de funciones trigonométricas."""
    print("📐 FUNCIONES TRIGONOMÉTRICAS")
    print("=" * 40)
    
    # Funciones en grados
    angulo = 90
    sen_90 = seno(angulo, en_radianes=False)
    cos_90 = coseno(angulo, en_radianes=False)
    tan_45 = tangente(45, en_radianes=False)
    
    print(f"sen(90°) = {sen_90:.6f}")
    print(f"cos(90°) = {cos_90:.6f}")
    print(f"tan(45°) = {tan_45:.6f}")
    
    # Funciones en radianes
    import math
    angulo_rad = math.pi / 4  # 45 grados en radianes
    sen_pi4 = seno(angulo_rad, en_radianes=True)
    cos_pi4 = coseno(angulo_rad, en_radianes=True)
    
    print(f"sen(π/4) = {sen_pi4:.6f}")
    print(f"cos(π/4) = {cos_pi4:.6f}")
    
    print()

def demo_operaciones_con_listas():
    """Demostración de operaciones con listas."""
    print("📊 OPERACIONES CON LISTAS")
    print("=" * 40)
    
    # Suma de lista
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = sumar_lista(numeros)
    print(f"Suma de {numeros} = {resultado}")
    
    # Multiplicación de lista
    numeros_pequenos = [2, 3, 4, 5]
    resultado = multiplicar_lista(numeros_pequenos)
    print(f"Multiplicación de {numeros_pequenos} = {resultado}")
    
    print()

def demo_manejo_errores():
    """Demostración del manejo de errores."""
    print("⚠️  MANEJO DE ERRORES")
    print("=" * 40)
    
    # División por cero
    try:
        resultado = dividir(10, 0)
    except ValueError as e:
        print(f"División por cero: {e}")
    
    # Raíz cuadrada de número negativo
    try:
        resultado = raiz_cuadrada(-25)
    except ValueError as e:
        print(f"Raíz cuadrada de negativo: {e}")
    
    # Logaritmo de número no válido
    try:
        resultado = logaritmo(0)
    except ValueError as e:
        print(f"Logaritmo de cero: {e}")
    
    # Factorial de número negativo
    try:
        resultado = factorial(-5)
    except ValueError as e:
        print(f"Factorial de negativo: {e}")
    
    print()

def main():
    """Función principal de la demostración."""
    print("🧮 DEMOSTRACIÓN DE LA CALCULADORA PROFESIONAL")
    print("=" * 60)
    print("Esta demostración muestra todas las funciones disponibles")
    print("=" * 60)
    print()
    
    demo_operaciones_basicas()
    demo_operaciones_avanzadas()
    demo_funciones_trigonometricas()
    demo_operaciones_con_listas()
    demo_manejo_errores()
    
    print("✅ DEMOSTRACIÓN COMPLETADA")
    print("=" * 60)
    print("Para usar la calculadora interactiva, ejecuta: python main.py")
    print("Para ejecutar los tests, ejecuta: python tests\\run_all_tests.py")

if __name__ == "__main__":
    main()
