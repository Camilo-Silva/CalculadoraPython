# tests/test_multiplicacion.py
# Tests para el módulo de multiplicación

import unittest
import sys
import os

# Agregar el directorio padre al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.multiplicacion import multiplicar, multiplicar_lista, potencia

class TestMultiplicacion(unittest.TestCase):
    """Tests para las funciones de multiplicación."""
    
    def test_multiplicar_positivos(self):
        """Test multiplicación de números positivos."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(7, 8), 56)
    
    def test_multiplicar_negativos(self):
        """Test multiplicación con números negativos."""
        self.assertEqual(multiplicar(-3, 4), -12)
        self.assertEqual(multiplicar(-3, -4), 12)
        self.assertEqual(multiplicar(3, -4), -12)
    
    def test_multiplicar_decimales(self):
        """Test multiplicación de números decimales."""
        self.assertAlmostEqual(multiplicar(2.5, 4), 10.0)
        self.assertAlmostEqual(multiplicar(3.14, 2), 6.28)
    
    def test_multiplicar_por_cero(self):
        """Test multiplicación por cero."""
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(0, 7), 0)
    
    def test_multiplicar_lista_vacia(self):
        """Test multiplicación de lista vacía."""
        self.assertEqual(multiplicar_lista([]), 0)
    
    def test_multiplicar_lista_un_elemento(self):
        """Test multiplicación de lista con un elemento."""
        self.assertEqual(multiplicar_lista([5]), 5)
    
    def test_multiplicar_lista_varios_elementos(self):
        """Test multiplicación de lista con varios elementos."""
        self.assertEqual(multiplicar_lista([2, 3, 4]), 24)
        self.assertEqual(multiplicar_lista([1, 2, 3, 4, 5]), 120)
    
    def test_potencia_normal(self):
        """Test potencia normal."""
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 2), 25)
        self.assertEqual(potencia(10, 0), 1)
    
    def test_potencia_negativa(self):
        """Test potencia con exponente negativo."""
        self.assertEqual(potencia(2, -2), 0.25)
        self.assertAlmostEqual(potencia(4, -1), 0.25)
    
    def test_potencia_decimal(self):
        """Test potencia con números decimales."""
        self.assertAlmostEqual(potencia(2.5, 2), 6.25)
        self.assertAlmostEqual(potencia(9, 0.5), 3.0)

if __name__ == '__main__':
    unittest.main()
