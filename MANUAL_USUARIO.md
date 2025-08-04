# MANUAL_USUARIO.md
# Manual de Usuario - Calculadora Profesional

## 📖 Guía Completa de Usuario

### 🚀 Inicio Rápido

#### Para usuarios principiantes:
1. Ejecuta `python main.py`
2. Selecciona la opción 2 (Interfaz gráfica)
3. ¡Comienza a calcular!

#### Para usuarios avanzados:
- Interfaz gráfica directa: `python main_gui.py`
- Interfaz de texto: `python main.py` → opción 1
- Demostración: `python demo.py`

---

## 🎨 Interfaz Gráfica - Guía Detallada

### 📱 Diseño de la Interfaz

La calculadora gráfica está organizada en secciones:

1. **Display Principal** (Superior)
   - Muestra números y resultados
   - Fuente grande y clara
   - Solo lectura (usa botones o teclado)

2. **Botones Básicos** (Centro)
   - Números (0-9) en blanco
   - Operaciones (+, -, ×, ÷) en verde
   - Funciones (√, x², etc.) en azul
   - Limpiar (C, CE) en rojo

3. **Pestañas de Funciones** (Centro-Inferior)
   - **Científica**: sin, cos, tan, log, ln, factorial, π, e
   - **Configuración**: Selección grados/radianes

4. **Historial** (Inferior)
   - Scroll automático
   - Botones para limpiar y copiar

### ⌨️ Uso del Teclado

| Tecla | Función |
|-------|---------|
| `0-9` | Ingresar números |
| `+` `-` `*` `/` | Operaciones básicas |
| `.` | Punto decimal |
| `Enter` o `=` | Calcular |
| `Delete` o `C` | Limpiar todo |
| `Escape` | Limpiar entrada |
| `Backspace` | Borrar último dígito |
| `Ctrl+N` | Nueva calculación |
| `Ctrl+C` | Copiar resultado |
| `F1` | Ayuda |

### 🔢 Operaciones Básicas

#### Suma, Resta, Multiplicación, División:
1. Ingresa el primer número
2. Presiona el operador (+, -, ×, ÷)
3. Ingresa el segundo número
4. Presiona `=` o `Enter`

**Ejemplo**: `15 + 25 = 40`

#### Operaciones Especiales:
- **x²**: Cuadrado del número actual
- **x³**: Cubo del número actual  
- **√**: Raíz cuadrada del número actual
- **x^y**: Potencia (ingresa base, presiona x^y, ingresa exponente, presiona =)

### 🧮 Funciones Científicas

#### Funciones Trigonométricas:
1. **Configurar unidad**: Ve a la pestaña "Configuración"
   - Selecciona "Grados" para trabajar en grados
   - Selecciona "Radianes" para trabajar en radianes

2. **Calcular**:
   - Ingresa el ángulo
   - Presiona `sin`, `cos`, o `tan`

**Ejemplos**:
- `sin(90°) = 1`
- `cos(0°) = 1`  
- `tan(45°) = 1`

#### Logaritmos:
- **log**: Logaritmo base 10
- **ln**: Logaritmo natural (base e)

**Ejemplos**:
- `log(100) = 2`
- `ln(e) = 1`

#### Factorial:
- Ingresa un número entero
- Presiona `n!`
- **Ejemplo**: `5! = 120`

#### Constantes:
- **π**: Presiona el botón π para insertar pi (3.14159...)
- **e**: Presiona el botón e para insertar e (2.71828...)

### 📊 Historial

El historial mantiene un registro de todas las operaciones:

- **Scroll automático**: Siempre muestra la operación más reciente
- **Capacidad**: Hasta 50 operaciones
- **Botones de control**:
  - `Limpiar Historial`: Borra todas las operaciones
  - `Copiar Última Operación`: Copia al portapapeles

### 🎛️ Menú Principal

#### Archivo:
- **Nueva calculación** (Ctrl+N): Limpia todo y comienza de nuevo
- **Salir** (Alt+F4): Cierra la aplicación

#### Editar:
- **Copiar resultado** (Ctrl+C): Copia el número del display
- **Limpiar** (Delete): Limpia todo
- **Limpiar entrada** (Escape): Solo limpia la entrada actual

#### Ver:
- **Limpiar historial**: Borra el historial
- **Copiar historial completo**: Copia todas las operaciones

#### Ayuda:
- **Atajos de teclado** (F1): Muestra esta ayuda
- **Acerca de**: Información de la aplicación

---

## 🖥️ Interfaz de Texto - Guía Detallada

### 📋 Navegación por Menús

La interfaz de texto presenta un menú numerado:

```
1.  Suma
2.  Resta  
3.  Multiplicación
4.  División
5.  Potencia
6.  Raíz cuadrada
7.  Logaritmo
8.  Factorial
9.  Funciones trigonométricas
10. Ver historial
11. Limpiar historial
0.  Salir
```

### 🔄 Flujo de Trabajo

1. **Seleccionar operación**: Ingresa el número de la opción
2. **Ingresar números**: Sigue las instrucciones en pantalla
3. **Ver resultado**: Se muestra automáticamente
4. **Continuar**: Presiona Enter para volver al menú

### 🔢 Ejemplos de Uso

#### Operaciones Básicas:
```
Seleccione una opción: 1
Ingrese el primer número: 25
Ingrese el segundo número: 15
Resultado: 25 + 15 = 40
```

#### Funciones Trigonométricas:
```
Seleccione una opción: 9
Funciones trigonométricas:
1. Seno
2. Coseno  
3. Tangente
Seleccione la función: 1
Ingrese el ángulo: 90
¿El ángulo está en:
1. Grados
2. Radianes
Opción: 1
Resultado: sen(90°) = 1.0
```

#### Logaritmos:
```
Seleccione una opción: 7
Seleccione la base del logaritmo:
1. Logaritmo natural (base e)
2. Logaritmo base 10
3. Base personalizada
Opción: 2
Ingrese el número: 1000
Resultado: log₁₀(1000) = 3.0
```

---

## ⚠️ Manejo de Errores

### Errores Comunes y Soluciones:

#### "No se puede dividir por cero"
- **Causa**: Intentaste dividir cualquier número por 0
- **Solución**: Usa un divisor diferente de cero

#### "No se puede calcular la raíz cuadrada de un número negativo"
- **Causa**: Intentaste calcular √(-número)
- **Solución**: Usa solo números positivos o cero

#### "El logaritmo no está definido para números menores o iguales a cero"
- **Causa**: Intentaste calcular log(0) o log(número negativo)
- **Solución**: Usa solo números positivos

#### "El factorial no está definido para números negativos"
- **Causa**: Intentaste calcular factorial de un número negativo
- **Solución**: Usa solo números enteros no negativos

#### "Número inválido"
- **Causa**: Ingresaste texto en lugar de números
- **Solución**: Ingresa solo números válidos

---

## 💡 Consejos y Trucos

### ⚡ Productividad:

1. **Usa atajos de teclado** en la interfaz gráfica para mayor velocidad
2. **Copia resultados** directamente con Ctrl+C
3. **Revisa el historial** para verificar cálculos anteriores
4. **Configura ángulos** antes de usar funciones trigonométricas

### 🎯 Precisión:

1. **Números decimales**: Usa punto (.) como separador decimal
2. **Números grandes**: La calculadora maneja números muy grandes
3. **Precisión**: Los resultados tienen precisión de punto flotante de Python

### 🔧 Solución de Problemas:

1. **Si la interfaz gráfica no abre**: Usa `python main.py` y selecciona opción 1
2. **Si hay errores de importación**: Ejecuta `python setup.py`
3. **Para reportar problemas**: Revisa el README.md

---

## 📞 Soporte

### 📚 Recursos Adicionales:
- **README.md**: Información técnica completa
- **demo.py**: Demostración de todas las funciones
- **tests/**: Tests unitarios para verificar funcionamiento

### 🔧 Resolución de Problemas:
1. Ejecuta `python setup.py` para verificar la instalación
2. Ejecuta `python tests/run_all_tests.py` para verificar funcionamiento
3. Consulta la documentación en README.md

---

¡Disfruta usando tu Calculadora Profesional! 🎉
