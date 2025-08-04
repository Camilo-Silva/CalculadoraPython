# tests/run_all_tests.py
# Script para ejecutar todos los tests de la calculadora

import unittest
import sys
import os

# Agregar el directorio padre al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():
    """Ejecuta todos los tests de la calculadora."""
    
    # Descubrir y ejecutar todos los tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Configurar el runner
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("="*60)
    print("         EJECUTANDO TESTS DE LA CALCULADORA")
    print("="*60)
    
    # Ejecutar los tests
    result = runner.run(suite)
    
    print("\n" + "="*60)
    if result.wasSuccessful():
        print("✅ TODOS LOS TESTS PASARON EXITOSAMENTE")
    else:
        print("❌ ALGUNOS TESTS FALLARON")
        print(f"Errores: {len(result.errors)}")
        print(f"Fallos: {len(result.failures)}")
    print("="*60)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
