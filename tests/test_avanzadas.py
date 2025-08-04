# tests/test_avanzadas.py
# Tests para el módulo de operaciones avanzadas

import unittest
import math
import sys
import os

# Agregar el directorio padre al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.avanzadas import raiz_cuadrada, logaritmo, factorial, seno, coseno

class TestAvanzadas(unittest.TestCase):
    """Tests para las funciones avanzadas."""
    
    def test_raiz_cuadrada_normal(self):
        """Test raíz cuadrada normal."""
        self.assertEqual(raiz_cuadrada(4), 2)
        self.assertEqual(raiz_cuadrada(9), 3)
        self.assertAlmostEqual(raiz_cuadrada(2), 1.4142135623730951)
    
    def test_raiz_cuadrada_negativo(self):
        """Test raíz cuadrada de número negativo."""
        with self.assertRaises(ValueError):
            raiz_cuadrada(-4)
    
    def test_logaritmo_natural(self):
        """Test logaritmo natural."""
        self.assertAlmostEqual(logaritmo(math.e), 1)
        self.assertAlmostEqual(logaritmo(1), 0)
    
    def test_logaritmo_base_10(self):
        """Test logaritmo base 10."""
        self.assertAlmostEqual(logaritmo(100, 10), 2)
        self.assertAlmostEqual(logaritmo(1000, 10), 3)
    
    def test_logaritmo_numero_invalido(self):
        """Test logaritmo de número inválido."""
        with self.assertRaises(ValueError):
            logaritmo(0)
        with self.assertRaises(ValueError):
            logaritmo(-5)
    
    def test_factorial_normal(self):
        """Test factorial normal."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
    
    def test_factorial_negativo(self):
        """Test factorial de número negativo."""
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_factorial_no_entero(self):
        """Test factorial de número no entero."""
        with self.assertRaises(ValueError):
            factorial(3.5)
    
    def test_funciones_trigonometricas(self):
        """Test funciones trigonométricas."""
        # Test en radianes
        self.assertAlmostEqual(seno(0), 0)
        self.assertAlmostEqual(coseno(0), 1)
        self.assertAlmostEqual(seno(math.pi/2), 1)
        
        # Test en grados
        self.assertAlmostEqual(seno(90, False), 1)
        self.assertAlmostEqual(coseno(90, False), 0, places=10)

if __name__ == '__main__':
    unittest.main()
