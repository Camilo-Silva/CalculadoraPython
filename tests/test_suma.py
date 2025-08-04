# tests/test_suma.py
# Tests para el módulo de suma

import unittest
import sys
import os

# Agregar el directorio padre al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.suma import sumar, sumar_lista

class TestSuma(unittest.TestCase):
    """Tests para las funciones de suma."""
    
    def test_sumar_positivos(self):
        """Test suma de números positivos."""
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(10, 15), 25)
    
    def test_sumar_negativos(self):
        """Test suma de números negativos."""
        self.assertEqual(sumar(-2, -3), -5)
        self.assertEqual(sumar(-10, 5), -5)
    
    def test_sumar_decimales(self):
        """Test suma de números decimales."""
        self.assertAlmostEqual(sumar(2.5, 3.7), 6.2)
        self.assertAlmostEqual(sumar(0.1, 0.2), 0.3)
    
    def test_sumar_lista_vacia(self):
        """Test suma de lista vacía."""
        self.assertEqual(sumar_lista([]), 0)
    
    def test_sumar_lista_un_elemento(self):
        """Test suma de lista con un elemento."""
        self.assertEqual(sumar_lista([5]), 5)
    
    def test_sumar_lista_varios_elementos(self):
        """Test suma de lista con varios elementos."""
        self.assertEqual(sumar_lista([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sumar_lista([-1, 1, -2, 2]), 0)

if __name__ == '__main__':
    unittest.main()
