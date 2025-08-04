# main.py
# Archivo principal de la calculadora

from modules.interfaz import Calculadora
from modules.interfaz_grafica import CalculadoraGUI

def mostrar_menu_inicio():
    """Muestra el menú de selección de interfaz."""
    print("="*50)
    print("    CALCULADORA PROFESIONAL EN PYTHON")
    print("="*50)
    print("Seleccione el tipo de interfaz:")
    print("1. Interfaz de texto (consola)")
    print("2. Interfaz gráfica (tkinter)")
    print("0. Salir")
    print("="*50)

if __name__ == "__main__":
    while True:
        mostrar_menu_inicio()
        
        try:
            opcion = input("Seleccione una opción (1, 2 o 0): ").strip()
            
            if opcion == "1":
                print("\nIniciando interfaz de texto...")
                calculadora = Calculadora()
                calculadora.ejecutar()
                break
            elif opcion == "2":
                print("\nIniciando interfaz gráfica...")
                try:
                    app = CalculadoraGUI()
                    app.run()
                    break
                except ImportError:
                    print("Error: tkinter no está disponible en su sistema.")
                    print("Use la opción 1 para la interfaz de texto.")
                    input("Presione Enter para continuar...")
                except Exception as e:
                    print(f"Error al iniciar la interfaz gráfica: {e}")
                    input("Presione Enter para continuar...")
            elif opcion == "0":
                print("¡Gracias por usar la calculadora!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
                input("Presione Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presione Enter para continuar...")
