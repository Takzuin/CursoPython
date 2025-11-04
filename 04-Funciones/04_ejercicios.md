# Ejercicios: Funciones 💪

Practica todo lo aprendido sobre funciones con estos ejercicios.

---

## Ejercicios Básicos

### 1. Función de saludo personalizado
Crea una función que reciba nombre y apellido, y retorne un saludo completo.

```python
def saludar_completo(nombre, apellido):
    # Tu código aquí
    pass

# Debe imprimir: "¡Hola, Juan Pérez! Bienvenido."
print(saludar_completo("Juan", "Pérez"))
```

---

### 2. Convertidor de temperatura
Crea dos funciones:
- `celsius_a_fahrenheit(celsius)`
- `fahrenheit_a_celsius(fahrenheit)`

Fórmulas:
- F = (C × 9/5) + 32
- C = (F - 32) × 5/9

```python
# Tu código aquí
```

---

### 3. Número par o impar
Escribe una función que retorne `True` si un número es par, `False` si es impar.

```python
def es_par(numero):
    # Tu código aquí
    pass
```

---

## Ejercicios Intermedios

### 4. Calculadora flexible
Crea una función que acepte dos números y una operación (por defecto "suma"):

```python
def calcular(a, b, operacion="suma"):
    # Soporta: suma, resta, multiplicacion, division
    # Tu código aquí
    pass

print(calcular(10, 5))              # 15
print(calcular(10, 5, "resta"))     # 5
print(calcular(10, 5, "multiplicacion"))  # 50
```

---

### 5. Contar vocales
Escribe una función que cuente cuántas vocales hay en una cadena:

```python
def contar_vocales(texto):
    # Tu código aquí
    pass

print(contar_vocales("Hola Mundo"))  # 4
```

---

### 6. Lista de números pares
Usa una función lambda con `filter()` para obtener solo los números pares de una lista:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Tu código aquí
```

---

### 7. Suma variable
Crea una función que acepte cualquier cantidad de números y retorne su suma:

```python
def sumar_todos(*numeros):
    # Tu código aquí
    pass

print(sumar_todos(1, 2, 3))           # 6
print(sumar_todos(10, 20, 30, 40))    # 100
```

---

## Ejercicios Avanzados

### 8. Fibonacci recursivo
Implementa la secuencia de Fibonacci de forma recursiva:

```python
def fibonacci(n):
    """
    Retorna el n-ésimo número de Fibonacci.
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    # Tu código aquí
    pass

print(fibonacci(7))  # 13
```

---

### 9. Validador de contraseña
Crea una función que valide si una contraseña cumple estos requisitos:
- Mínimo 8 caracteres
- Al menos una letra mayúscula
- Al menos una letra minúscula
- Al menos un número

```python
def validar_contrasena(contrasena):
    # Tu código aquí
    pass

print(validar_contrasena("Abc12345"))  # True
print(validar_contrasena("abc123"))    # False (sin mayúscula)
```

---

### 10. Generador de estadísticas
Crea una función que reciba una lista de números y retorne un diccionario con estadísticas:

```python
def estadisticas(numeros):
    """
    Retorna un diccionario con:
    - promedio
    - maximo
    - minimo
    - suma
    """
    # Tu código aquí
    pass

print(estadisticas([1, 2, 3, 4, 5]))
# {'promedio': 3.0, 'maximo': 5, 'minimo': 1, 'suma': 15}
```

---

### 11. Decorador de tiempo
Crea un decorador que mida cuánto tarda en ejecutarse una función:

```python
import time

def medir_tiempo(func):
    # Tu código aquí
    pass

@medir_tiempo
def operacion_lenta():
    time.sleep(1)
    return "Completado"

operacion_lenta()
# Debe imprimir algo como: "Tiempo de ejecución: 1.001 segundos"
```

---

### 12. Función de búsqueda
Crea una función que busque un valor en una lista recursivamente:

```python
def buscar(lista, valor, indice=0):
    """
    Retorna el índice del valor en la lista, o -1 si no existe.
    Usa recursión.
    """
    # Tu código aquí
    pass

print(buscar([1, 3, 5, 7, 9], 5))   # 2
print(buscar([1, 3, 5, 7, 9], 4))   # -1
```

---

## Proyectos Mini

### 13. Sistema de calificaciones
Crea un conjunto de funciones para manejar calificaciones:

```python
def agregar_calificacion(estudiante, calificaciones, nota):
    """Agrega una calificación a la lista del estudiante."""
    pass

def calcular_promedio(calificaciones):
    """Calcula el promedio de una lista de calificaciones."""
    pass

def letra_calificacion(promedio):
    """Retorna la letra (A, B, C, D, F) según el promedio."""
    # 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    pass

# Ejemplo de uso:
calificaciones_juan = []
agregar_calificacion("Juan", calificaciones_juan, 85)
agregar_calificacion("Juan", calificaciones_juan, 90)
promedio = calcular_promedio(calificaciones_juan)
print(f"Promedio: {promedio}, Calificación: {letra_calificacion(promedio)}")
```

---

### 14. Calculadora con historial
Crea una calculadora que mantenga un historial de operaciones usando closures:

```python
def crear_calculadora():
    """
    Retorna una función calculadora que mantiene historial.
    La calculadora debe tener métodos para:
    - realizar operaciones
    - ver historial
    - limpiar historial
    """
    # Tu código aquí
    pass

# Ejemplo de uso:
calc = crear_calculadora()
calc.sumar(5, 3)
calc.multiplicar(2, 4)
calc.mostrar_historial()
```

---

## 🎯 Tips para resolver

1. **Lee el problema completo** antes de empezar a escribir código
2. **Piensa en casos especiales**: ¿qué pasa con listas vacías? ¿números negativos? ¿cadenas vacías?
3. **Prueba con diferentes entradas** para asegurarte de que funciona
4. **Documenta tus funciones** con docstrings
5. **Usa nombres descriptivos** para variables y funciones

---

## 📚 Soluciones

Las soluciones están disponibles en `soluciones/04-Funciones/`.

¡Intenta resolver los ejercicios por ti mismo primero! La lucha es parte del aprendizaje. 💪

---

**¡Felicidades!** 🎉 Has completado el módulo de Funciones. Ahora tienes las herramientas para escribir código reutilizable y organizado.

**Próximo módulo:** Estructuras de Datos (Listas, Diccionarios, Tuplas, Conjuntos)
