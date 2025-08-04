# main_gui.py
# Archivo principal para ejecutar la calculadora con interfaz gráfica

from modules.interfaz_grafica import CalculadoraGUI

if __name__ == "__main__":
    print("Iniciando Calculadora Profesional - Interfaz Gráfica")
    app = CalculadoraGUI()
    app.run()
