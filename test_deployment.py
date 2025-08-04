#!/usr/bin/env python3
"""
Script de prueba para verificar que el deployment funcione correctamente
"""

import sys
import os

# Agregar el directorio de módulos al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def test_import_modules():
    """Prueba que todos los módulos se puedan importar correctamente"""
    print("🧪 Probando importación de módulos...")
    
    try:
        # Probar importaciones básicas
        from modules.suma import sumar
        from modules.resta import restar
        from modules.multiplicacion import multiplicar
        from modules.division import dividir
        from modules.avanzadas import raiz_cuadrada, factorial
        print("✅ Módulos matemáticos importados correctamente")
        
        # Probar importación de la interfaz CLI
        from modules.interfaz import Calculadora
        print("✅ Interfaz CLI importada correctamente")
        
        # Probar importación condicional de GUI
        try:
            from modules.interfaz_grafica import CalculadoraGUI
            print("✅ Interfaz gráfica disponible")
        except ImportError:
            print("⚠️ Interfaz gráfica no disponible (normal en contenedores)")
        
    except ImportError as e:
        print(f"❌ Error importando módulos: {e}")
        return False
    
    return True

def test_app_import():
    """Prueba que la aplicación Flask se pueda importar"""
    print("\n🧪 Probando importación de la aplicación Flask...")
    
    try:
        from app import app
        print("✅ Aplicación Flask importada correctamente")
        print(f"✅ Nombre de la app: {app.name}")
        return True
    except ImportError as e:
        print(f"❌ Error importando la aplicación Flask: {e}")
        return False

def test_basic_calculations():
    """Prueba cálculos básicos"""
    print("\n🧪 Probando cálculos básicos...")
    
    try:
        from modules.suma import sumar
        from modules.multiplicacion import multiplicar
        from modules.avanzadas import raiz_cuadrada
        
        # Probar operaciones
        assert sumar(2, 3) == 5
        assert multiplicar(4, 5) == 20
        assert raiz_cuadrada(16) == 4.0
        
        print("✅ Cálculos básicos funcionando correctamente")
        return True
    except Exception as e:
        print(f"❌ Error en cálculos básicos: {e}")
        return False

def test_flask_routes():
    """Prueba que las rutas de Flask funcionen"""
    print("\n🧪 Probando rutas de Flask...")
    
    try:
        from app import app
        
        with app.test_client() as client:
            # Probar ruta principal
            response = client.get('/')
            assert response.status_code == 200
            print("✅ Ruta principal (/) funciona")
            
            # Probar API de cálculo
            response = client.post('/api/calculate', 
                                 json={'operation': 'basic', 'num1': 5, 'num2': 3, 'operator': '+'})
            assert response.status_code == 200
            data = response.get_json()
            assert data['result'] == 8
            print("✅ API de cálculo funciona")
            
        return True
    except Exception as e:
        print(f"❌ Error en rutas de Flask: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando pruebas de deployment...\n")
    
    tests = [
        test_import_modules,
        test_app_import,
        test_basic_calculations,
        test_flask_routes
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Resultados: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El proyecto está listo para deployment.")
        sys.exit(0)
    else:
        print("❌ Algunas pruebas fallaron. Revisar los errores antes del deployment.")
        sys.exit(1)

if __name__ == "__main__":
    main()
