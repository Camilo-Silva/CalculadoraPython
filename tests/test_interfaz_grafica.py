# tests/test_interfaz_grafica.py
# Tests para la interfaz gráfica de la calculadora

import unittest
import sys
import os

# Agregar el directorio padre al path para importar modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import tkinter as tk
    from modules.interfaz_grafica import CalculadoraGUI
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False

@unittest.skipUnless(TKINTER_AVAILABLE, "tkinter no está disponible")
class TestCalculadoraGUI(unittest.TestCase):
    """Tests para la interfaz gráfica de la calculadora."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.app = CalculadoraGUI()
    
    def tearDown(self):
        """Limpieza después de cada test."""
        if hasattr(self, 'app') and self.app.root:
            self.app.root.destroy()
    
    def test_inicializacion(self):
        """Test inicialización de la aplicación."""
        self.assertIsNotNone(self.app.root)
        self.assertEqual(self.app.display_var.get(), "0")
        self.assertEqual(self.app.operation, "")
        self.assertEqual(self.app.previous_value, 0)
        self.assertEqual(self.app.current_value, 0)
        self.assertFalse(self.app.result_shown)
    
    def test_number_click(self):
        """Test clic en números."""
        self.app.number_click("5")
        self.assertEqual(self.app.display_var.get(), "5")
        
        self.app.number_click("3")
        self.assertEqual(self.app.display_var.get(), "53")
        
        # Test punto decimal
        self.app.clear()
        self.app.number_click(".")
        self.assertEqual(self.app.display_var.get(), "0.")
    
    def test_operation_click(self):
        """Test clic en operaciones."""
        self.app.number_click("5")
        self.app.operation_click("+")
        
        self.assertEqual(self.app.operation, "+")
        self.assertEqual(self.app.previous_value, 5.0)
        self.assertTrue(self.app.result_shown)
    
    def test_equals_click(self):
        """Test clic en igual."""
        # Configurar operación: 5 + 3
        self.app.number_click("5")
        self.app.operation_click("+")
        self.app.number_click("3")
        self.app.equals_click()
        
        self.assertEqual(self.app.display_var.get(), "8")
    
    def test_clear(self):
        """Test función limpiar."""
        self.app.number_click("5")
        self.app.operation_click("+")
        self.app.clear()
        
        self.assertEqual(self.app.display_var.get(), "0")
        self.assertEqual(self.app.operation, "")
        self.assertEqual(self.app.previous_value, 0)
        self.assertFalse(self.app.result_shown)
    
    def test_square_root(self):
        """Test raíz cuadrada."""
        self.app.display_var.set("9")
        self.app.square_root()
        self.assertEqual(self.app.display_var.get(), "3.0")
    
    def test_square(self):
        """Test cuadrado."""
        self.app.display_var.set("4")
        self.app.square()
        self.assertEqual(self.app.display_var.get(), "16")
    
    def test_toggle_sign(self):
        """Test cambio de signo."""
        self.app.display_var.set("5")
        self.app.toggle_sign()
        self.assertEqual(self.app.display_var.get(), "-5.0")
        
        self.app.toggle_sign()
        self.assertEqual(self.app.display_var.get(), "5.0")
    
    def test_backspace(self):
        """Test retroceso."""
        self.app.display_var.set("123")
        self.app.backspace()
        self.assertEqual(self.app.display_var.get(), "12")
        
        self.app.backspace()
        self.app.backspace()
        self.assertEqual(self.app.display_var.get(), "0")
    
    def test_history(self):
        """Test historial."""
        # Verificar que el historial esté vacío
        self.assertEqual(len(self.app.historial), 0)
        
        # Agregar operación al historial
        self.app.add_to_history("5 + 3 = 8")
        self.assertEqual(len(self.app.historial), 1)
        self.assertEqual(self.app.historial[0], "5 + 3 = 8")
        
        # Limpiar historial
        self.app.clear_history()
        self.assertEqual(len(self.app.historial), 0)

if __name__ == '__main__':
    if TKINTER_AVAILABLE:
        unittest.main()
    else:
        print("tkinter no está disponible. Saltando tests de interfaz gráfica.")
