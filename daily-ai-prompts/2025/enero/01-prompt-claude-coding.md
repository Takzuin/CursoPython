# 💻 Prompt de Coding: Refactorización y Clean Code

**Plataforma:** Claude 3.5 Sonnet
**Fecha:** 01 de Enero, 2025
**Tags:** #coding #python #cleancode #refactoring

---

## 📝 El Prompt

```text
Tienes el siguiente código en Python que funciona pero está mal escrito, sin tipado y es difícil de leer:

```python
def calc(x,y,z):
  if z==1: return x+y
  if z==2: return x-y
  # ... más lógica confusa ...
```

Por favor:
1. Refactoriza el código aplicando principios SOLID y Clean Code.
2. Agrega Type Hints (anotaciones de tipo).
3. Incluye Docstrings explicativos.
4. Sugiere 3 casos de prueba unitaria usando `pytest`.

Explica brevemente por qué tus cambios mejoran el código.
```

## 💡 Por qué funciona

Claude 3.5 Sonnet destaca en tareas de programación. Al pedir explícitamente **SOLID** y **Clean Code**, obligas al modelo a elevar la calidad del output más allá de "simplemente que funcione".

## 🚀 Beneficio

Obtendrás código más mantenible, legible y robusto, ideal para aprendizaje o para mejorar bases de código legacy.
