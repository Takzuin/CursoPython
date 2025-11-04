# Funciones Avanzadas 🚀

Exploremos conceptos más avanzados de funciones en Python.

---

## Docstrings - Documentar funciones

Los **docstrings** son cadenas de documentación que describen qué hace una función:

```python
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo
    """
    return base * altura

# Puedes acceder a la documentación con help()
help(calcular_area_rectangulo)
```

**Formato simple:**
```python
def saludar(nombre):
    """Retorna un saludo personalizado."""
    return f"¡Hola, {nombre}!"
```

---

## Scope (Ámbito de variables)

El **scope** determina dónde puedes acceder a una variable.

### Variables locales

Las variables creadas dentro de una función solo existen ahí:

```python
def mi_funcion():
    x = 10  # Variable local
    print(x)

mi_funcion()  # 10
# print(x)    # ❌ Error: x no existe fuera de la función
```

### Variables globales

Las variables creadas fuera de funciones son globales:

```python
x = 10  # Variable global

def mostrar():
    print(x)  # Puede leer la variable global

mostrar()  # 10
```

### Modificar variables globales

Para modificar una variable global dentro de una función, usa `global`:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)  # 2
```

**⚠️ Cuidado:** Usar `global` demasiado puede hacer tu código difícil de mantener. Mejor usa `return`:

```python
# ✅ Mejor práctica
def incrementar(valor):
    return valor + 1

contador = 0
contador = incrementar(contador)
contador = incrementar(contador)
print(contador)  # 2
```

---

## Funciones Lambda (Anónimas)

Las funciones lambda son funciones pequeñas de una sola línea:

```python
# Función normal
def cuadrado(x):
    return x ** 2

# Función lambda equivalente
cuadrado = lambda x: x ** 2

print(cuadrado(5))  # 25
```

**Sintaxis:**
```python
lambda parametros: expresion
```

### ¿Cuándo usar lambda?

Lambda es útil para funciones simples que usas una sola vez:

```python
numeros = [1, 2, 3, 4, 5]

# Con función normal
def cuadrado(x):
    return x ** 2

cuadrados = list(map(cuadrado, numeros))

# Con lambda (más conciso)
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]
```

### Múltiples parámetros

```python
suma = lambda a, b: a + b
print(suma(3, 5))  # 8

mayor = lambda a, b: a if a > b else b
print(mayor(10, 5))  # 10
```

---

## Funciones como objetos

En Python, las funciones son objetos de primera clase:

```python
def saludar():
    return "¡Hola!"

# Asignar función a una variable
mi_funcion = saludar
print(mi_funcion())  # ¡Hola!

# Pasar función como argumento
def ejecutar_funcion(func):
    return func()

print(ejecutar_funcion(saludar))  # ¡Hola!
```

---

## Recursión

Una función recursiva es aquella que se llama a sí misma:

```python
def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

print(factorial(5))  # 5! = 5 × 4 × 3 × 2 × 1 = 120
```

**Componentes de la recursión:**
1. **Caso base**: Condición que detiene la recursión
2. **Llamada recursiva**: La función se llama a sí misma

### Ejemplo: Suma de lista

```python
def suma_lista(lista):
    """Suma los elementos de una lista recursivamente."""
    if len(lista) == 0:  # Caso base
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])  # Recursión

print(suma_lista([1, 2, 3, 4, 5]))  # 15
```

**⚠️ Cuidado:** La recursión puede causar errores si no hay caso base o si la pila de llamadas es muy profunda.

---

## Funciones anidadas

Puedes definir funciones dentro de otras funciones:

```python
def exterior(x):
    def interior(y):
        return y ** 2
    
    return interior(x) + 10

print(exterior(5))  # 25 + 10 = 35
```

---

## Closures

Un closure es una función que recuerda valores del ámbito donde fue creada:

```python
def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

multiplicar_por_3 = crear_multiplicador(3)
multiplicar_por_5 = crear_multiplicador(5)

print(multiplicar_por_3(10))  # 30
print(multiplicar_por_5(10))  # 50
```

---

## Decoradores (Introducción básica)

Los decoradores modifican el comportamiento de funciones:

```python
def mi_decorador(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
# Salida:
# Antes de la función
# ¡Hola!
# Después de la función
```

---

## 💡 Buenas prácticas

1. **Funciones puras**: Evita efectos secundarios
   ```python
   # ✅ Función pura (no modifica nada externo)
   def suma(a, b):
       return a + b
   
   # ❌ No pura (modifica variable global)
   total = 0
   def sumar_al_total(x):
       global total
       total += x
   ```

2. **DRY (Don't Repeat Yourself)**: Si copias código, probablemente necesitas una función

3. **Principio de responsabilidad única**: Una función = Una tarea

4. **Nombres descriptivos**: `calcular_promedio()` es mejor que `calc()`

---

## 💪 Ejercicios

1. Escribe una función recursiva para calcular números de Fibonacci.

2. Crea un decorador que mida el tiempo de ejecución de una función.

3. Escribe una función que use lambda para filtrar números pares de una lista.

4. Crea una función con docstring completo que calcule el área de un círculo.

5. Implementa una función recursiva que invierta una cadena de texto.

---

**Siguiente:** [Ejercicios de Funciones](04_ejercicios.md)
