# modules/interfaz_grafica.py
# Interfaz gráfica de la calculadora usando tkinter

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math
from . import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, logaritmo, factorial,
    seno, coseno, tangente
)

class CalculadoraGUI:
    """Interfaz gráfica para la calculadora profesional."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora Profesional - Python")
        self.root.geometry("500x700")
        self.root.resizable(True, True)
        
        # Variables
        self.display_var = tk.StringVar(value="0")
        self.operation = ""
        self.previous_value = 0
        self.current_value = 0
        self.result_shown = False
        self.historial = []
        
        # Configurar estilo
        self.setup_style()
        
        # Crear menú
        self.create_menu()
          # Crear interfaz
        self.create_widgets()
        
        # Configurar teclado
        self.setup_keyboard_bindings()
    
    def setup_style(self):
        """Configura el estilo visual de la aplicación."""
        self.root.configure(bg='#f0f0f0')
        
        # Estilo para botones
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('Number.TButton', 
                       background='#ffffff',
                       foreground='#333333',
                       font=('Arial', 12))
        
        style.configure('Operation.TButton',
                       background='#4CAF50',
                       foreground='white',
                       font=('Arial', 12, 'bold'))
        
        style.configure('Function.TButton',
                       background='#2196F3',
                       foreground='white',
                       font=('Arial', 10))
        
        style.configure('Clear.TButton',
                       background='#f44336',
                       foreground='white',
                       font=('Arial', 12, 'bold'))
    
    def create_menu(self):
        """Crea la barra de menú."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nueva calculación", command=self.clear, accelerator="Ctrl+N")
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit, accelerator="Alt+F4")
        
        # Menú Editar
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Copiar resultado", command=self.copy_result, accelerator="Ctrl+C")
        edit_menu.add_command(label="Limpiar", command=self.clear, accelerator="Delete")
        edit_menu.add_command(label="Limpiar entrada", command=self.clear_entry, accelerator="Escape")
        
        # Menú Ver
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ver", menu=view_menu)
        view_menu.add_command(label="Limpiar historial", command=self.clear_history)
        view_menu.add_command(label="Copiar historial completo", command=self.copy_full_history)
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Atajos de teclado", command=self.show_keyboard_shortcuts)
        help_menu.add_command(label="Acerca de", command=self.show_about)
    
    def create_widgets(self):
        """Crea todos los widgets de la interfaz."""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Crear display
        self.create_display(main_frame)
        
        # Crear botones básicos
        self.create_basic_buttons(main_frame)
        
        # Crear pestañas para funciones avanzadas
        self.create_advanced_tabs(main_frame)
        
        # Crear área de historial
        self.create_history_area(main_frame)
    
    def create_display(self, parent):
        """Crea el área de visualización."""
        display_frame = ttk.Frame(parent)
        display_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        display_frame.columnconfigure(0, weight=1)
        
        # Display principal
        display = tk.Entry(display_frame, 
                          textvariable=self.display_var,
                          font=('Arial', 20, 'bold'),
                          justify='right',
                          state='readonly',
                          bg='white',
                          relief='sunken',
                          bd=2)
        display.grid(row=0, column=0, sticky=(tk.W, tk.E), ipady=10)
    
    def create_basic_buttons(self, parent):
        """Crea los botones básicos de la calculadora."""
        buttons_frame = ttk.Frame(parent)
        buttons_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Configurar grid para botones
        for i in range(5):
            buttons_frame.columnconfigure(i, weight=1)
        
        # Fila 0: Funciones especiales
        ttk.Button(buttons_frame, text="C", style='Clear.TButton',
                  command=self.clear).grid(row=0, column=0, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="CE", style='Clear.TButton',
                  command=self.clear_entry).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="←", style='Function.TButton',
                  command=self.backspace).grid(row=0, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="±", style='Function.TButton',
                  command=self.toggle_sign).grid(row=0, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="√", style='Function.TButton',
                  command=self.square_root).grid(row=0, column=4, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Fila 1
        ttk.Button(buttons_frame, text="7", style='Number.TButton',
                  command=lambda: self.number_click("7")).grid(row=1, column=0, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="8", style='Number.TButton',
                  command=lambda: self.number_click("8")).grid(row=1, column=1, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="9", style='Number.TButton',
                  command=lambda: self.number_click("9")).grid(row=1, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="÷", style='Operation.TButton',
                  command=lambda: self.operation_click("÷")).grid(row=1, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="x²", style='Function.TButton',
                  command=self.square).grid(row=1, column=4, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Fila 2
        ttk.Button(buttons_frame, text="4", style='Number.TButton',
                  command=lambda: self.number_click("4")).grid(row=2, column=0, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="5", style='Number.TButton',
                  command=lambda: self.number_click("5")).grid(row=2, column=1, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="6", style='Number.TButton',
                  command=lambda: self.number_click("6")).grid(row=2, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="×", style='Operation.TButton',
                  command=lambda: self.operation_click("×")).grid(row=2, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="x³", style='Function.TButton',
                  command=self.cube).grid(row=2, column=4, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Fila 3
        ttk.Button(buttons_frame, text="1", style='Number.TButton',
                  command=lambda: self.number_click("1")).grid(row=3, column=0, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="2", style='Number.TButton',
                  command=lambda: self.number_click("2")).grid(row=3, column=1, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="3", style='Number.TButton',
                  command=lambda: self.number_click("3")).grid(row=3, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="-", style='Operation.TButton',
                  command=lambda: self.operation_click("-")).grid(row=3, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="x^y", style='Function.TButton',
                  command=lambda: self.operation_click("^")).grid(row=3, column=4, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Fila 4
        ttk.Button(buttons_frame, text="0", style='Number.TButton',
                  command=lambda: self.number_click("0")).grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text=".", style='Number.TButton',
                  command=lambda: self.number_click(".")).grid(row=4, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="+", style='Operation.TButton',
                  command=lambda: self.operation_click("+")).grid(row=4, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(buttons_frame, text="=", style='Operation.TButton',
                  command=self.equals_click).grid(row=4, column=4, sticky=(tk.W, tk.E), padx=2, pady=2)
    
    def create_advanced_tabs(self, parent):
        """Crea las pestañas para funciones avanzadas."""
        notebook = ttk.Notebook(parent)
        notebook.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Pestaña de funciones científicas
        sci_frame = ttk.Frame(notebook, padding="5")
        notebook.add(sci_frame, text="Científica")
        
        # Configurar grid
        for i in range(4):
            sci_frame.columnconfigure(i, weight=1)
        
        # Botones científicos
        ttk.Button(sci_frame, text="sin", style='Function.TButton',
                  command=self.sin_click).grid(row=0, column=0, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(sci_frame, text="cos", style='Function.TButton',
                  command=self.cos_click).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(sci_frame, text="tan", style='Function.TButton',
                  command=self.tan_click).grid(row=0, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(sci_frame, text="log", style='Function.TButton',
                  command=self.log_click).grid(row=0, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        ttk.Button(sci_frame, text="ln", style='Function.TButton',
                  command=self.ln_click).grid(row=1, column=0, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(sci_frame, text="n!", style='Function.TButton',
                  command=self.factorial_click).grid(row=1, column=1, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(sci_frame, text="π", style='Function.TButton',
                  command=lambda: self.number_click(str(math.pi))).grid(row=1, column=2, sticky=(tk.W, tk.E), padx=2, pady=2)
        ttk.Button(sci_frame, text="e", style='Function.TButton',
                  command=lambda: self.number_click(str(math.e))).grid(row=1, column=3, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Pestaña de configuración
        config_frame = ttk.Frame(notebook, padding="5")
        notebook.add(config_frame, text="Configuración")
        
        # Opciones de ángulos
        ttk.Label(config_frame, text="Unidad de ángulos:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.angle_mode = tk.StringVar(value="degrees")
        ttk.Radiobutton(config_frame, text="Grados", variable=self.angle_mode, 
                       value="degrees").grid(row=1, column=0, sticky=tk.W)
        ttk.Radiobutton(config_frame, text="Radianes", variable=self.angle_mode, 
                       value="radians").grid(row=2, column=0, sticky=tk.W)
    
    def create_history_area(self, parent):
        """Crea el área de historial."""
        history_frame = ttk.LabelFrame(parent, text="Historial", padding="5")
        history_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 5))
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(0, weight=1)
        parent.rowconfigure(3, weight=1)
          # Área de texto con scroll
        self.history_text = scrolledtext.ScrolledText(history_frame, 
                                                     height=6,
                                                     width=50,
                                                     font=('Consolas', 9),
                                                     state='disabled')
        self.history_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Botones de historial
        history_buttons = ttk.Frame(history_frame)
        history_buttons.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))
        
        ttk.Button(history_buttons, text="Limpiar Historial",
                  command=self.clear_history).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(history_buttons, text="Copiar Última Operación",
                  command=self.copy_last_operation).pack(side=tk.LEFT)
    
    def setup_keyboard_bindings(self):
        """Configura los atajos de teclado."""
        self.root.bind('<Key>', self.key_press)
        
        # Atajos adicionales del menú
        self.root.bind('<Control-n>', lambda e: self.clear())
        self.root.bind('<Control-c>', lambda e: self.copy_result())
        self.root.bind('<F1>', lambda e: self.show_keyboard_shortcuts())
        
        self.root.focus_set()
    
    def key_press(self, event):
        """Maneja las pulsaciones de teclado."""
        key = event.char
        
        if key.isdigit() or key == '.':
            self.number_click(key)
        elif key in ['+', '-', '*', '/']:
            if key == '*':
                key = '×'
            elif key == '/':
                key = '÷'
            self.operation_click(key)
        elif key == '\r' or key == '=':  # Enter o =
            self.equals_click()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Delete' or key.lower() == 'c':
            self.clear()
        elif event.keysym == 'Escape':
            self.clear_entry()
    
    def number_click(self, number):
        """Maneja el clic en botones numéricos."""
        current = self.display_var.get()
        
        if self.result_shown or current == "0":
            if number == ".":
                self.display_var.set("0.")
            else:
                self.display_var.set(number)
            self.result_shown = False
        else:
            if number == "." and "." in current:
                return  # Ya hay un punto decimal
            self.display_var.set(current + number)
    
    def operation_click(self, op):
        """Maneja el clic en botones de operación."""
        try:
            if self.operation and not self.result_shown:
                self.equals_click()
            
            self.previous_value = float(self.display_var.get())
            self.operation = op
            self.result_shown = True
        except ValueError:
            self.show_error("Número inválido")
    
    def equals_click(self):
        """Maneja el clic en el botón igual."""
        try:
            if not self.operation:
                return
            
            self.current_value = float(self.display_var.get())
            result = self.calculate()
            
            if result is not None:
                # Formatear el resultado
                if result == int(result):
                    result = int(result)
                
                self.display_var.set(str(result))
                
                # Agregar al historial
                operation_str = f"{self.previous_value} {self.operation} {self.current_value} = {result}"
                self.add_to_history(operation_str)
                
                self.operation = ""
                self.result_shown = True
        except (ValueError, ZeroDivisionError) as e:
            self.show_error(str(e))
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def calculate(self):
        """Realiza el cálculo según la operación."""
        try:
            if self.operation == "+":
                return sumar(self.previous_value, self.current_value)
            elif self.operation == "-":
                return restar(self.previous_value, self.current_value)
            elif self.operation == "×":
                return multiplicar(self.previous_value, self.current_value)
            elif self.operation == "÷":
                return dividir(self.previous_value, self.current_value)
            elif self.operation == "^":
                return potencia(self.previous_value, self.current_value)
            else:
                return None
        except ValueError as e:
            raise e
    
    def square_root(self):
        """Calcula la raíz cuadrada."""
        try:
            value = float(self.display_var.get())
            result = raiz_cuadrada(value)
            self.display_var.set(str(result))
            self.add_to_history(f"√{value} = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def square(self):
        """Calcula el cuadrado."""
        try:
            value = float(self.display_var.get())
            result = potencia(value, 2)
            self.display_var.set(str(result))
            self.add_to_history(f"{value}² = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def cube(self):
        """Calcula el cubo."""
        try:
            value = float(self.display_var.get())
            result = potencia(value, 3)
            self.display_var.set(str(result))
            self.add_to_history(f"{value}³ = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def sin_click(self):
        """Calcula el seno."""
        try:
            value = float(self.display_var.get())
            en_radianes = self.angle_mode.get() == "radians"
            result = seno(value, en_radianes)
            
            unit = "rad" if en_radianes else "°"
            self.display_var.set(str(result))
            self.add_to_history(f"sin({value}{unit}) = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def cos_click(self):
        """Calcula el coseno."""
        try:
            value = float(self.display_var.get())
            en_radianes = self.angle_mode.get() == "radians"
            result = coseno(value, en_radianes)
            
            unit = "rad" if en_radianes else "°"
            self.display_var.set(str(result))
            self.add_to_history(f"cos({value}{unit}) = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def tan_click(self):
        """Calcula la tangente."""
        try:
            value = float(self.display_var.get())
            en_radianes = self.angle_mode.get() == "radians"
            result = tangente(value, en_radianes)
            
            unit = "rad" if en_radianes else "°"
            self.display_var.set(str(result))
            self.add_to_history(f"tan({value}{unit}) = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def log_click(self):
        """Calcula el logaritmo base 10."""
        try:
            value = float(self.display_var.get())
            result = logaritmo(value, 10)
            self.display_var.set(str(result))
            self.add_to_history(f"log₁₀({value}) = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def ln_click(self):
        """Calcula el logaritmo natural."""
        try:
            value = float(self.display_var.get())
            result = logaritmo(value)
            self.display_var.set(str(result))
            self.add_to_history(f"ln({value}) = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def factorial_click(self):
        """Calcula el factorial."""
        try:
            value = int(float(self.display_var.get()))
            result = factorial(value)
            self.display_var.set(str(result))
            self.add_to_history(f"{value}! = {result}")
            self.result_shown = True
        except ValueError as e:
            self.show_error(str(e))
    
    def toggle_sign(self):
        """Cambia el signo del número."""
        try:
            value = float(self.display_var.get())
            self.display_var.set(str(-value))
        except ValueError:
            pass
    
    def clear(self):
        """Limpia todo."""
        self.display_var.set("0")
        self.operation = ""
        self.previous_value = 0
        self.current_value = 0
        self.result_shown = False
    
    def clear_entry(self):
        """Limpia solo la entrada actual."""
        self.display_var.set("0")
        self.result_shown = False
    
    def backspace(self):
        """Elimina el último dígito."""
        current = self.display_var.get()
        if len(current) > 1:
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")
    
    def add_to_history(self, operation):
        """Agrega una operación al historial."""
        self.historial.append(operation)
        if len(self.historial) > 50:  # Mantener solo las últimas 50 operaciones
            self.historial.pop(0)
        
        # Actualizar el display del historial
        self.history_text.config(state='normal')
        self.history_text.insert(tk.END, operation + "\n")
        self.history_text.see(tk.END)
        self.history_text.config(state='disabled')
    
    def clear_history(self):
        """Limpia el historial."""
        self.historial.clear()
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state='disabled')
    
    def copy_last_operation(self):
        """Copia la última operación al portapapeles."""
        if self.historial:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.historial[-1])
            messagebox.showinfo("Copiado", "Última operación copiada al portapapeles")
    
    def show_error(self, message):
        """Muestra un mensaje de error."""
        messagebox.showerror("Error", message)
        self.clear()
    
    def copy_result(self):
        """Copia el resultado actual al portapapeles."""
        self.root.clipboard_clear()
        self.root.clipboard_append(self.display_var.get())
        messagebox.showinfo("Copiado", "Resultado copiado al portapapeles")
    
    def copy_full_history(self):
        """Copia todo el historial al portapapeles."""
        if self.historial:
            full_history = "\n".join(self.historial)
            self.root.clipboard_clear()
            self.root.clipboard_append(full_history)
            messagebox.showinfo("Copiado", "Historial completo copiado al portapapeles")
        else:
            messagebox.showinfo("Historial vacío", "No hay operaciones en el historial")
    
    def show_keyboard_shortcuts(self):
        """Muestra los atajos de teclado disponibles."""
        shortcuts_text = """
⌨️ ATAJOS DE TECLADO

🔢 NÚMEROS Y OPERACIONES:
• 0-9: Ingresar números
• +, -, *, /: Operaciones básicas
• .: Punto decimal
• Enter o =: Calcular resultado

🎛️ CONTROLES:
• Delete o C: Limpiar todo
• Escape: Limpiar entrada actual
• Backspace: Borrar último dígito

📋 MENÚ:
• Ctrl+N: Nueva calculación
• Ctrl+C: Copiar resultado
• Alt+F4: Salir

🔧 FUNCIONES:
• Los botones de funciones científicas
  solo están disponibles con clic del mouse
        """
        
        # Crear ventana de ayuda
        help_window = tk.Toplevel(self.root)
        help_window.title("Atajos de Teclado")
        help_window.geometry("400x500")
        help_window.resizable(False, False)
        
        # Centrar la ventana
        help_window.transient(self.root)
        help_window.grab_set()
        
        # Texto de ayuda
        text_widget = tk.Text(help_window, wrap=tk.WORD, padx=20, pady=20, 
                             font=('Consolas', 10), state='disabled')
        text_widget.pack(fill=tk.BOTH, expand=True)
        
        text_widget.config(state='normal')
        text_widget.insert(tk.END, shortcuts_text)
        text_widget.config(state='disabled')
        
        # Botón cerrar
        close_btn = ttk.Button(help_window, text="Cerrar", 
                              command=help_window.destroy)
        close_btn.pack(pady=10)
    
    def show_about(self):
        """Muestra información sobre la aplicación."""
        about_text = """
🧮 CALCULADORA PROFESIONAL

Versión: 2.0
Fecha: Julio 2025

Desarrollada en Python con tkinter
Estructura modular y testing completo

✨ CARACTERÍSTICAS:
• Operaciones básicas y avanzadas
• Funciones trigonométricas
• Historial completo
• Interfaz moderna
• Atajos de teclado

👨‍💻 DESARROLLADOR:
Calculadora profesional creada con
las mejores prácticas de desarrollo

📄 LICENCIA: MIT
        """
        
        messagebox.showinfo("Acerca de Calculadora Profesional", about_text)
    
    def run(self):
        """Ejecuta la aplicación."""
        self.root.mainloop()

def main():
    """Función principal para ejecutar la interfaz gráfica."""
    app = CalculadoraGUI()
    app.run()

if __name__ == "__main__":
    main()
