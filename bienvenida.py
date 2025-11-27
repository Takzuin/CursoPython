#!/usr/bin/env python3
"""
Script de bienvenida al CursoPython
===================================

Este script verifica que Python esté correctamente instalado
y da la bienvenida al curso.
"""

import sys
import platform

def mostrar_bienvenida():
    """Muestra mensaje de bienvenida y información del sistema."""
    
    print("=" * 60)
    print("   ¡BIENVENIDO AL CURSO DE PYTHON! 🐍")
    print("=" * 60)
    print()
    
    # Información del sistema
    print("📊 Información de tu sistema:")
    print(f"   • Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"   • Versión de Python: {sys.version.split()[0]}")
    print(f"   • Ejecutable: {sys.executable}")
    print()
    
    # Verificar versión de Python
    version_info = sys.version_info
    if version_info.major >= 3 and version_info.minor >= 6:
        print("✅ Tu versión de Python es compatible con este curso")
    else:
        print("⚠️  Se recomienda Python 3.6 o superior")
    
    print()
    print("=" * 60)
    print("   ESTRUCTURA DEL CURSO")
    print("=" * 60)
    print()
    print("📁 01-Introduccion/       → Comienza aquí")
    print("📁 02-Variables&Tipos/    → Variables y tipos de datos")
    print("📁 03-Control-de-Flujo/   → If/else y bucles")
    print("📁 04-Funciones/          → Funciones y parámetros")
    print("📁 ... y mucho más! (POO, Archivos, Estructuras de Datos)")
    print()
    print("Cada carpeta contiene:")
    print("  • README.md - Introducción al módulo")
    print("  • Lecciones numeradas (01_tema.md, 02_tema.md, ...)")
    print("  • Ejercicios prácticos")
    print("  • Carpeta ejemplos/ con código ejecutable")
    print()
    print("=" * 60)
    print("   CÓMO USAR ESTE CURSO")
    print("=" * 60)
    print()
    print("1️⃣  Lee las lecciones en orden")
    print("2️⃣  Ejecuta los ejemplos en tu computadora")
    print("3️⃣  Resuelve los ejercicios por ti mismo")
    print("4️⃣  Experimenta y modifica el código")
    print()
    print("💡 Consejo: No te saltes los ejercicios. La práctica es clave.")
    print()
    print("=" * 60)
    print("   RECURSOS ADICIONALES")
    print("=" * 60)
    print()
    print("📖 Documentación oficial: https://docs.python.org/es/3/")
    print("🐛 Reportar problemas: https://github.com/takzuin/CursoPython/issues")
    print("🤝 Contribuir: Lee CONTRIBUTING.md")
    print()
    print("=" * 60)
    print()
    print("¿Listo para empezar? 🚀")
    print("Navega a la carpeta 01-Introduccion/ y comienza tu viaje.")
    print()
    print("¡Mucha suerte y diviértete aprendiendo! 💪")
    print()

if __name__ == "__main__":
    mostrar_bienvenida()
