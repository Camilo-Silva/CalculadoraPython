# tests/test_division.py
# Tests para el módulo de división

import unittest
import sys
import os

# Agregar el directorio padre al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.division import dividir, division_entera, modulo

class TestDivision(unittest.TestCase):
    """Tests para las funciones de división."""
    
    def test_dividir_normal(self):
        """Test división normal."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(15, 3), 5)
        self.assertAlmostEqual(dividir(7, 3), 2.333333333333333)
    
    def test_dividir_por_cero(self):
        """Test división por cero."""
        with self.assertRaises(ValueError):
            dividir(10, 0)
    
    def test_division_entera_normal(self):
        """Test división entera normal."""
        self.assertEqual(division_entera(10, 3), 3)
        self.assertEqual(division_entera(15, 4), 3)
    
    def test_division_entera_por_cero(self):
        """Test división entera por cero."""
        with self.assertRaises(ValueError):
            division_entera(10, 0)
    
    def test_modulo_normal(self):
        """Test operación módulo normal."""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 4), 3)
        self.assertEqual(modulo(8, 4), 0)
    
    def test_modulo_por_cero(self):
        """Test operación módulo por cero."""
        with self.assertRaises(ValueError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
