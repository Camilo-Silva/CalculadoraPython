# setup.py
# Script de configuración e instalación para la calculadora

import sys
import os
import subprocess

def check_python_version():
    """Verifica que la versión de Python sea compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("❌ Error: Se requiere Python 3.6 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True

def check_tkinter():
    """Verifica si tkinter está disponible."""
    try:
        import tkinter
        print("✅ tkinter disponible - Interfaz gráfica habilitada")
        return True
    except ImportError:
        print("⚠️  tkinter no disponible - Solo interfaz de texto")
        print("   En Linux: sudo apt-get install python3-tk")
        return False

def run_tests():
    """Ejecuta todos los tests para verificar la instalación."""
    print("\n🧪 Ejecutando tests...")
    try:
        result = subprocess.run([
            sys.executable, "tests/run_all_tests.py"
        ], capture_output=True, text=True, cwd=os.path.dirname(__file__))
        
        if result.returncode == 0:
            print("✅ Todos los tests pasaron exitosamente")
            return True
        else:
            print("❌ Algunos tests fallaron:")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error ejecutando tests: {e}")
        return False

def create_shortcuts():
    """Crea scripts de acceso directo."""
    shortcuts = {
        "calculadora.bat": [
            "@echo off",
            f"cd /d \"{os.path.dirname(os.path.abspath(__file__))}\"",
            "python main.py",
            "pause"
        ],
        "calculadora_gui.bat": [
            "@echo off",
            f"cd /d \"{os.path.dirname(os.path.abspath(__file__))}\"",
            "python main_gui.py",
            "pause"
        ],
        "demo.bat": [
            "@echo off",
            f"cd /d \"{os.path.dirname(os.path.abspath(__file__))}\"",
            "python demo.py",
            "pause"
        ]
    }
    
    print("\n📝 Creando accesos directos...")
    for filename, content in shortcuts.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))
            print(f"   ✅ {filename}")
        except Exception as e:
            print(f"   ❌ Error creando {filename}: {e}")

def show_usage_info():
    """Muestra información de uso."""
    print("\n" + "="*60)
    print("🎉 ¡INSTALACIÓN COMPLETADA!")
    print("="*60)
    print("📋 Formas de ejecutar la calculadora:")
    print()
    print("1️⃣  Selector de interfaz:")
    print("   python main.py")
    print("   O hacer doble clic en: calculadora.bat")
    print()
    print("2️⃣  Interfaz gráfica directa:")
    print("   python main_gui.py")
    print("   O hacer doble clic en: calculadora_gui.bat")
    print()
    print("3️⃣  Demostración:")
    print("   python demo.py")
    print("   O hacer doble clic en: demo.bat")
    print()
    print("4️⃣  Ejecutar tests:")
    print("   python tests\\run_all_tests.py")
    print()
    print("="*60)
    print("📚 Consulta README.md para más información")
    print("="*60)

def main():
    """Función principal del setup."""
    print("🧮 CONFIGURACIÓN DE CALCULADORA PROFESIONAL")
    print("="*50)
    
    # Verificar requisitos
    if not check_python_version():
        sys.exit(1)
    
    tkinter_available = check_tkinter()
    
    # Ejecutar tests
    if not run_tests():
        print("\n⚠️  Los tests fallaron, pero la instalación puede continuar")
        response = input("¿Desea continuar? (s/n): ").lower()
        if response not in ['s', 'sí', 'si', 'y', 'yes']:
            sys.exit(1)
    
    # Crear accesos directos (solo en Windows)
    if os.name == 'nt':
        create_shortcuts()
    
    # Mostrar información final
    show_usage_info()
    
    # Ofrecer ejecutar la calculadora
    print("\n¿Desea ejecutar la calculadora ahora?")
    if tkinter_available:
        print("1. Interfaz gráfica")
        print("2. Interfaz de texto")
        print("3. No ejecutar")
        choice = input("Seleccione (1/2/3): ").strip()
        
        if choice == "1":
            subprocess.run([sys.executable, "main_gui.py"])
        elif choice == "2":
            subprocess.run([sys.executable, "main.py"])
    else:
        response = input("¿Ejecutar interfaz de texto? (s/n): ").lower()
        if response in ['s', 'sí', 'si', 'y', 'yes']:
            subprocess.run([sys.executable, "main.py"])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Instalación cancelada por el usuario")
    except Exception as e:
        print(f"\n❌ Error durante la instalación: {e}")
        sys.exit(1)
