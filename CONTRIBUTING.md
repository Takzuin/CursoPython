# Contribuir a CursoPython 🤝

¡Gracias por tu interés en mejorar este curso! Toda contribución es bienvenida.

---

## Formas de contribuir

### 🐛 Reportar errores
- Abre un **issue** describiendo el error
- Include el archivo y línea donde está el problema
- Si es un error de código, incluye el mensaje de error

### 💡 Sugerir mejoras
- Abre un **issue** con la etiqueta "enhancement"
- Describe qué te gustaría mejorar y por qué
- Si es contenido nuevo, explica qué tema cubriría

### 📝 Corregir errores
- Haz un **fork** del repositorio
- Crea una rama con un nombre descriptivo: `fix/corregir-ejemplo-bucles`
- Realiza tus cambios
- Envía un **pull request**

### ➕ Añadir contenido
- Abre un **issue** primero para discutir el contenido
- Sigue la estructura existente de carpetas y archivos
- Mantén el estilo de escritura: claro, amigable y con ejemplos

---

## Guía de estilo

### Estructura de archivos
```
XX-Nombre-Modulo/
├── README.md           # Introducción al módulo
├── 01_tema.md          # Primera lección
├── 02_tema.md          # Segunda lección
└── 03_ejercicios.md    # Ejercicios prácticos
```

### Formato Markdown
- Usa títulos claros y jerárquicos (`#`, `##`, `###`)
- Incluye bloques de código con sintaxis highlighting:
  ````markdown
  ```python
  print("Hola, mundo!")
  ```
  ````
- Añade emojis para hacer el contenido más visual (pero sin abusar)
- Usa listas numeradas para pasos secuenciales
- Usa listas con viñetas para opciones/características

### Código de ejemplo
- **Claro y simple**: Evita complejidad innecesaria
- **Comentado**: Explica las partes no obvias
- **Ejecutable**: Todo código debe funcionar sin errores
- **Didáctico**: Prioriza la enseñanza sobre la eficiencia

**Ejemplo:**
```python
# ✅ Bien: claro y didáctico
nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} años")

# ❌ Evitar: código muy avanzado para principiantes
print(f"Hola, me llamo {(lambda x: x.capitalize())('ana')} y tengo {sum([20, 5])} años")
```

---

## Proceso de pull request

1. **Fork** el repositorio
2. **Clona** tu fork localmente:
   ```bash
   git clone https://github.com/TU_USUARIO/CursoPython.git
   ```
3. **Crea una rama** para tus cambios:
   ```bash
   git checkout -b mi-mejora
   ```
4. **Realiza tus cambios** y haz commits descriptivos:
   ```bash
   git add .
   git commit -m "Añadir ejemplos de listas en módulo 5"
   ```
5. **Push** a tu fork:
   ```bash
   git push origin mi-mejora
   ```
6. **Abre un Pull Request** en GitHub
7. Describe qué cambios hiciste y por qué

---

## Criterios de aceptación

Para que tu PR sea aceptado, debe:

✅ Seguir la guía de estilo del proyecto  
✅ No contener errores de sintaxis o ortografía  
✅ Incluir ejemplos funcionales (si aplica)  
✅ Ser apropiado para el nivel del módulo  
✅ Tener una descripción clara en el PR  

---

## Código de conducta

- Sé respetuoso con todos los colaboradores
- Acepta feedback constructivo
- Enfócate en mejorar el contenido para los estudiantes
- No uses lenguaje ofensivo o inapropiado

---

## ¿Necesitas ayuda?

Si tienes dudas sobre cómo contribuir:
- Abre un **issue** con tus preguntas
- Revisa los PRs anteriores como referencia
- Contacta al mantenedor del repositorio

---

**¡Gracias por hacer este curso mejor para todos!** 🌟
