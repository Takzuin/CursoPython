# Funciones Básicas en Python 🔧

Las funciones son bloques de código que puedes reutilizar tantas veces como necesites. En lugar de escribir el mismo código una y otra vez, defines una función y la llamas cuando la necesites.

---

## Definir una función

Para crear una función en Python usamos la palabra clave `def`:

```python
def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()  # Imprime: ¡Hola, mundo!
```

---

## Funciones con parámetros

Los parámetros permiten pasar información a la función:

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Ana")    # ¡Hola, Ana!
saludar("Carlos") # ¡Hola, Carlos!
```

### Múltiples parámetros

```python
def suma(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

suma(5, 3)   # 5 + 3 = 8
suma(10, 20) # 10 + 20 = 30
```

---

## La sentencia `return`

`return` devuelve un valor desde la función:

```python
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)  # 8

# Puedes usar el resultado directamente
print(suma(10, 20))  # 30
```

**Diferencia importante:**
- `print()`: Muestra algo en pantalla
- `return`: Devuelve un valor que puedes usar después

```python
def funcion_con_print(x):
    print(x * 2)

def funcion_con_return(x):
    return x * 2

a = funcion_con_print(5)   # Imprime 10, pero a = None
b = funcion_con_return(5)  # No imprime nada, pero b = 10
```

---

## Funciones sin `return`

Si no usas `return`, la función devuelve `None` automáticamente:

```python
def saludar():
    print("Hola")

resultado = saludar()  # Imprime: Hola
print(resultado)        # Imprime: None
```

---

## Retornar múltiples valores

Python permite retornar múltiples valores como una tupla:

```python
def calcular(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

s, r, m = calcular(10, 5)
print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}")
```

---

## Parámetros con valores por defecto

Puedes dar valores por defecto a los parámetros:

```python
def saludar(nombre="amigo"):
    print(f"¡Hola, {nombre}!")

saludar()         # ¡Hola, amigo!
saludar("María")  # ¡Hola, María!
```

```python
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))      # 9 (3²)
print(potencia(3, 3))   # 27 (3³)
```

---

## Ejemplo práctico: Calculadora

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Usar las funciones
print(sumar(10, 5))       # 15
print(restar(10, 5))      # 5
print(multiplicar(10, 5)) # 50
print(dividir(10, 5))     # 2.0
print(dividir(10, 0))     # Error: División por cero
```

---

## 💡 Buenas prácticas

1. **Nombres descriptivos**: Usa nombres que describan qué hace la función
   ```python
   # ✅ Bien
   def calcular_area_circulo(radio):
       return 3.14159 * radio ** 2
   
   # ❌ Mal
   def f(r):
       return 3.14159 * r ** 2
   ```

2. **Una función, una tarea**: Cada función debe hacer una cosa y hacerla bien

3. **Documenta tu código**: Usa docstrings (veremos esto más adelante)

---

## 💪 Ejercicios

1. Crea una función `es_par(numero)` que retorne `True` si el número es par, `False` si no.

2. Escribe una función `calcular_promedio(a, b, c)` que retorne el promedio de tres números.

3. Crea una función `celsius_a_fahrenheit(celsius)` que convierta grados Celsius a Fahrenheit.
   - Fórmula: F = (C × 9/5) + 32

4. Escribe una función `mayor_de_tres(a, b, c)` que retorne el mayor de tres números.

---

**Siguiente:** [Parámetros y Argumentos](02_parametros.md)
