# tests/test_resta.py
# Tests para el módulo de resta

import unittest
import sys
import os

# Agregar el directorio padre al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.resta import restar, restar_lista

class TestResta(unittest.TestCase):
    """Tests para las funciones de resta."""
    
    def test_restar_positivos(self):
        """Test resta de números positivos."""
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(10, 4), 6)
    
    def test_restar_negativos(self):
        """Test resta con números negativos."""
        self.assertEqual(restar(-5, -3), -2)
        self.assertEqual(restar(5, -3), 8)
        self.assertEqual(restar(-5, 3), -8)
    
    def test_restar_decimales(self):
        """Test resta de números decimales."""
        self.assertAlmostEqual(restar(5.5, 2.3), 3.2)
        self.assertAlmostEqual(restar(0.5, 0.3), 0.2)
    
    def test_restar_lista_vacia(self):
        """Test resta de lista vacía."""
        self.assertEqual(restar_lista([]), 0)
    
    def test_restar_lista_un_elemento(self):
        """Test resta de lista con un elemento."""
        self.assertEqual(restar_lista([5]), 5)
    
    def test_restar_lista_varios_elementos(self):
        """Test resta secuencial de lista con varios elementos."""
        self.assertEqual(restar_lista([10, 3, 2]), 5)  # 10 - 3 - 2 = 5
        self.assertEqual(restar_lista([20, 5, 3, 2]), 10)  # 20 - 5 - 3 - 2 = 10

if __name__ == '__main__':
    unittest.main()
