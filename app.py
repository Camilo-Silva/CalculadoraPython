# app.py
# Aplicación web Flask para calculadora

from flask import Flask, render_template, request, jsonify
import sys
import os

# Agregar el directorio de módulos al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

# Importar módulos de la calculadora
from suma import sumar, sumar_lista
from resta import restar, restar_lista
from multiplicacion import multiplicar, multiplicar_lista, potencia
from division import dividir, division_entera, modulo
from avanzadas import raiz_cuadrada, raiz_n, logaritmo, factorial, seno, coseno, tangente

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal de la calculadora"""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API endpoint para realizar cálculos"""
    try:
        data = request.get_json()
        operation = data.get('operation')
        
        if operation == 'basic':
            # Operaciones básicas
            num1 = float(data.get('num1', 0))
            num2 = float(data.get('num2', 0))
            operator = data.get('operator')
            
            if operator == '+':
                result = sumar(num1, num2)
            elif operator == '-':
                result = restar(num1, num2)
            elif operator == '*':
                result = multiplicar(num1, num2)
            elif operator == '/':
                result = dividir(num1, num2)
            elif operator == '//':
                result = division_entera(num1, num2)
            elif operator == '%':
                result = modulo(num1, num2)
            elif operator == '**':
                result = potencia(num1, num2)
            else:
                return jsonify({'error': 'Operador no válido'}), 400
                
        elif operation == 'advanced':
            # Operaciones avanzadas
            func = data.get('function')
            num = float(data.get('number', 0))
            
            if func == 'sqrt':
                result = raiz_cuadrada(num)
            elif func == 'factorial':
                result = factorial(int(num))
            elif func == 'ln':
                result = logaritmo(num)
            elif func == 'log10':
                result = logaritmo(num, 10)
            elif func == 'sin':
                result = seno(num)
            elif func == 'cos':
                result = coseno(num)
            elif func == 'tan':
                result = tangente(num)
            elif func == 'root_n':
                n = float(data.get('n', 2))
                result = raiz_n(num, n)
            else:
                return jsonify({'error': 'Función no válida'}), 400
                
        elif operation == 'list':
            # Operaciones con listas
            numbers = [float(x) for x in data.get('numbers', [])]
            operator = data.get('operator')
            
            if operator == 'sum':
                result = sumar_lista(numbers)
            elif operator == 'subtract':
                result = restar_lista(numbers)
            elif operator == 'multiply':
                result = multiplicar_lista(numbers)
            else:
                return jsonify({'error': 'Operación de lista no válida'}), 400
        else:
            return jsonify({'error': 'Tipo de operación no válido'}), 400
            
        return jsonify({'result': result})
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500

@app.route('/api/history')
def get_history():
    """Endpoint para obtener historial de cálculos (placeholder)"""
    # Aquí podrías implementar un sistema de historial si lo deseas
    return jsonify({'history': []})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
