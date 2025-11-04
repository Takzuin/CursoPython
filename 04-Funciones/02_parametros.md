# Parámetros y Argumentos 📝

Profundicemos en cómo pasar información a las funciones de diferentes maneras.

---

## Terminología

- **Parámetro**: Variable en la definición de la función
- **Argumento**: Valor que pasas cuando llamas a la función

```python
def saludar(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}")

saludar("Ana")  # "Ana" es un argumento
```

---

## Argumentos posicionales

Los argumentos se asignan a los parámetros según su posición:

```python
def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

presentar("Ana", 25, "Madrid")
# Me llamo Ana, tengo 25 años y vivo en Madrid
```

**El orden importa:**
```python
presentar("Madrid", "Ana", 25)
# Me llamo Madrid, tengo Ana años y vivo en 25 ❌
```

---

## Argumentos con nombre (keyword arguments)

Puedes especificar el nombre del parámetro al pasar argumentos:

```python
def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

# El orden no importa cuando usas nombres
presentar(edad=25, ciudad="Madrid", nombre="Ana")
presentar(ciudad="Madrid", nombre="Ana", edad=25)
```

---

## Mezclar argumentos posicionales y con nombre

Puedes mezclar ambos, pero **los posicionales deben ir primero**:

```python
def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

# ✅ Correcto
presentar("Ana", edad=25, ciudad="Madrid")

# ❌ Error: argumentos posicionales después de keyword arguments
# presentar(nombre="Ana", 25, "Madrid")
```

---

## Parámetros con valores por defecto

Ya vimos esto antes, pero veamos más detalles:

```python
def crear_usuario(nombre, edad=18, pais="España"):
    print(f"Usuario: {nombre}, {edad} años, de {pais}")

crear_usuario("Ana")                    # Usuario: Ana, 18 años, de España
crear_usuario("Carlos", 30)             # Usuario: Carlos, 30 años, de España
crear_usuario("María", 25, "México")    # Usuario: María, 25 años, de México
crear_usuario("Juan", pais="Argentina") # Usuario: Juan, 18 años, de Argentina
```

**Importante:** Los parámetros con valores por defecto deben ir después de los que no tienen valores por defecto:

```python
# ✅ Correcto
def funcion(a, b, c=10):
    pass

# ❌ Error
def funcion(a, b=5, c):  # SyntaxError
    pass
```

---

## `*args` - Número variable de argumentos posicionales

Usa `*args` cuando no sabes cuántos argumentos recibirás:

```python
def sumar_todos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2, 3))           # 6
print(sumar_todos(10, 20, 30, 40))    # 100
print(sumar_todos(5))                 # 5
```

`*args` crea una **tupla** con todos los argumentos:

```python
def mostrar_args(*args):
    print(f"Tipo: {type(args)}")
    print(f"Contenido: {args}")

mostrar_args(1, 2, 3, "hola")
# Tipo: <class 'tuple'>
# Contenido: (1, 2, 3, 'hola')
```

---

## `**kwargs` - Número variable de argumentos con nombre

Usa `**kwargs` para aceptar cualquier número de argumentos con nombre:

```python
def crear_perfil(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Ana", edad=25, ciudad="Madrid")
# nombre: Ana
# edad: 25
# ciudad: Madrid

crear_perfil(usuario="carlos123", email="carlos@email.com", pais="México")
# usuario: carlos123
# email: carlos@email.com
# pais: México
```

`**kwargs` crea un **diccionario**:

```python
def mostrar_kwargs(**kwargs):
    print(f"Tipo: {type(kwargs)}")
    print(f"Contenido: {kwargs}")

mostrar_kwargs(a=1, b=2, c=3)
# Tipo: <class 'dict'>
# Contenido: {'a': 1, 'b': 2, 'c': 3}
```

---

## Combinar todo

Puedes combinar diferentes tipos de parámetros, **respetando este orden**:

1. Parámetros normales
2. `*args`
3. Parámetros con nombre y valores por defecto
4. `**kwargs`

```python
def funcion_completa(a, b, *args, opcion=None, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"opcion: {opcion}")
    print(f"kwargs: {kwargs}")

funcion_completa(1, 2, 3, 4, 5, opcion="test", x=10, y=20)
# a: 1
# b: 2
# args: (3, 4, 5)
# opcion: test
# kwargs: {'x': 10, 'y': 20}
```

---

## Desempaquetar argumentos

Puedes desempaquetar listas/tuplas con `*` y diccionarios con `**`:

```python
def suma(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
print(suma(*numeros))  # Equivalente a suma(1, 2, 3)

datos = {'a': 10, 'b': 20, 'c': 30}
print(suma(**datos))  # Equivalente a suma(a=10, b=20, c=30)
```

---

## 💡 Ejercicios

1. Crea una función `multiplicar_todos(*numeros)` que multiplique todos los números pasados.

2. Escribe una función `info_persona(**datos)` que imprima la información de una persona de forma bonita.

3. Crea una función `calcular(a, b, operacion="suma")` que realice diferentes operaciones según el parámetro `operacion` (suma, resta, multiplicacion, division).

4. Escribe una función que acepte una lista de números y retorne el promedio usando desempaquetado.

---

**Siguiente:** [Funciones Avanzadas](03_funciones_avanzadas.md)
