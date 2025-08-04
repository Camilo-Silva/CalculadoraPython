# modules/interfaz.py
# Módulo para la interfaz de usuario de la calculadora

import sys
from . import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, logaritmo, factorial,
    seno, coseno, tangente
)

class Calculadora:
    """Clase principal de la calculadora con interfaz de usuario."""
    
    def __init__(self):
        self.historial = []
    
    def mostrar_menu(self):
        """Muestra el menú principal de la calculadora."""
        print("\n" + "="*50)
        print("         CALCULADORA PROFESIONAL")
        print("="*50)
        print("1.  Suma")
        print("2.  Resta")
        print("3.  Multiplicación")
        print("4.  División")
        print("5.  Potencia")
        print("6.  Raíz cuadrada")
        print("7.  Logaritmo")
        print("8.  Factorial")
        print("9.  Funciones trigonométricas")
        print("10. Ver historial")
        print("11. Limpiar historial")
        print("0.  Salir")
        print("="*50)
    
    def obtener_numeros(self, cantidad=2):
        """
        Obtiene números del usuario.
        
        Args:
            cantidad (int): Cantidad de números a solicitar
        
        Returns:
            list: Lista de números ingresados
        """
        numeros = []
        for i in range(cantidad):
            while True:
                try:
                    numero = float(input(f"Ingrese el número {i+1}: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido.")
        return numeros
    
    def agregar_al_historial(self, operacion, resultado):
        """
        Agrega una operación al historial.
        
        Args:
            operacion (str): Descripción de la operación
            resultado (float): Resultado de la operación
        """
        self.historial.append(f"{operacion} = {resultado}")
        if len(self.historial) > 20:  # Mantener solo las últimas 20 operaciones
            self.historial.pop(0)
    
    def mostrar_resultado(self, operacion, resultado):
        """
        Muestra el resultado de una operación.
        
        Args:
            operacion (str): Descripción de la operación
            resultado (float): Resultado de la operación
        """
        print(f"\nResultado: {operacion} = {resultado}")
        self.agregar_al_historial(operacion, resultado)
    
    def operaciones_basicas(self, opcion):
        """Maneja las operaciones matemáticas básicas."""
        numeros = self.obtener_numeros(2)
        a, b = numeros[0], numeros[1]
        
        try:
            if opcion == 1:  # Suma
                resultado = sumar(a, b)
                self.mostrar_resultado(f"{a} + {b}", resultado)
            elif opcion == 2:  # Resta
                resultado = restar(a, b)
                self.mostrar_resultado(f"{a} - {b}", resultado)
            elif opcion == 3:  # Multiplicación
                resultado = multiplicar(a, b)
                self.mostrar_resultado(f"{a} × {b}", resultado)
            elif opcion == 4:  # División
                resultado = dividir(a, b)
                self.mostrar_resultado(f"{a} ÷ {b}", resultado)
            elif opcion == 5:  # Potencia
                resultado = potencia(a, b)
                self.mostrar_resultado(f"{a}^{b}", resultado)
        except ValueError as e:
            print(f"Error: {e}")
    
    def operaciones_avanzadas(self, opcion):
        """Maneja las operaciones matemáticas avanzadas."""
        if opcion == 6:  # Raíz cuadrada
            numeros = self.obtener_numeros(1)
            try:
                resultado = raiz_cuadrada(numeros[0])
                self.mostrar_resultado(f"√{numeros[0]}", resultado)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == 7:  # Logaritmo
            print("Seleccione la base del logaritmo:")
            print("1. Logaritmo natural (base e)")
            print("2. Logaritmo base 10")
            print("3. Base personalizada")
            
            while True:
                try:
                    base_opcion = int(input("Opción: "))
                    if base_opcion in [1, 2, 3]:
                        break
                    print("Opción inválida.")
                except ValueError:
                    print("Ingrese un número válido.")
            
            numeros = self.obtener_numeros(1)
            numero = numeros[0]
            
            try:
                if base_opcion == 1:
                    resultado = logaritmo(numero)
                    self.mostrar_resultado(f"ln({numero})", resultado)
                elif base_opcion == 2:
                    resultado = logaritmo(numero, 10)
                    self.mostrar_resultado(f"log₁₀({numero})", resultado)
                else:
                    base = float(input("Ingrese la base: "))
                    resultado = logaritmo(numero, base)
                    self.mostrar_resultado(f"log_{base}({numero})", resultado)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == 8:  # Factorial
            while True:
                try:
                    numero = int(input("Ingrese un número entero: "))
                    break
                except ValueError:
                    print("Error: Ingrese un número entero válido.")
            
            try:
                resultado = factorial(numero)
                self.mostrar_resultado(f"{numero}!", resultado)
            except ValueError as e:
                print(f"Error: {e}")
    
    def funciones_trigonometricas(self):
        """Maneja las funciones trigonométricas."""
        print("\nFunciones trigonométricas:")
        print("1. Seno")
        print("2. Coseno")
        print("3. Tangente")
        
        while True:
            try:
                func_opcion = int(input("Seleccione la función: "))
                if func_opcion in [1, 2, 3]:
                    break
                print("Opción inválida.")
            except ValueError:
                print("Ingrese un número válido.")
        
        angulo = float(input("Ingrese el ángulo: "))
        
        print("¿El ángulo está en:")
        print("1. Grados")
        print("2. Radianes")
        unidad = int(input("Opción: "))
        en_radianes = unidad == 2
        
        try:
            if func_opcion == 1:  # Seno
                resultado = seno(angulo, en_radianes)
                unidad_str = "rad" if en_radianes else "°"
                self.mostrar_resultado(f"sen({angulo}{unidad_str})", resultado)
            elif func_opcion == 2:  # Coseno
                resultado = coseno(angulo, en_radianes)
                unidad_str = "rad" if en_radianes else "°"
                self.mostrar_resultado(f"cos({angulo}{unidad_str})", resultado)
            elif func_opcion == 3:  # Tangente
                resultado = tangente(angulo, en_radianes)
                unidad_str = "rad" if en_radianes else "°"
                self.mostrar_resultado(f"tan({angulo}{unidad_str})", resultado)
        except Exception as e:
            print(f"Error: {e}")
    
    def mostrar_historial(self):
        """Muestra el historial de operaciones."""
        if not self.historial:
            print("\nEl historial está vacío.")
        else:
            print("\n" + "="*30)
            print("       HISTORIAL")
            print("="*30)
            for i, operacion in enumerate(self.historial, 1):
                print(f"{i:2}. {operacion}")
            print("="*30)
    
    def limpiar_historial(self):
        """Limpia el historial de operaciones."""
        self.historial.clear()
        print("\nHistorial limpiado.")
    
    def ejecutar(self):
        """Ejecuta la calculadora con su interfaz de usuario."""
        print("Bienvenido a la calculadora profesional en Python.")
        
        while True:
            self.mostrar_menu()
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 0:  # Salir
                    print("\n¡Gracias por usar la calculadora!")
                    sys.exit()
                elif 1 <= opcion <= 5:  # Operaciones básicas
                    self.operaciones_basicas(opcion)
                elif 6 <= opcion <= 8:  # Operaciones avanzadas
                    self.operaciones_avanzadas(opcion)
                elif opcion == 9:  # Funciones trigonométricas
                    self.funciones_trigonometricas()
                elif opcion == 10:  # Ver historial
                    self.mostrar_historial()
                elif opcion == 11:  # Limpiar historial
                    self.limpiar_historial()
                else:
                    print("Opción inválida. Intente nuevamente.")
                
                input("\nPresione Enter para continuar...")
                
            except ValueError:
                print("Error: Ingrese un número válido.")
                input("\nPresione Enter para continuar...")
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego!")
                sys.exit()
            except Exception as e:
                print(f"Error inesperado: {e}")
                input("\nPresione Enter para continuar...")
