# Bucles en Python 🔄

Los bucles permiten ejecutar un bloque de código múltiples veces. Python tiene dos tipos principales de bucles: `for` y `while`.

---

## El bucle `for`

El bucle `for` se usa para iterar sobre una secuencia (lista, rango, cadena, etc.):

```python
# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)
```

**Salida:**
```
manzana
banana
naranja
```

---

## La función `range()`

`range()` genera una secuencia de números y es muy útil con `for`:

```python
# range(inicio, fin, paso)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

---

## El bucle `while`

El bucle `while` se ejecuta mientras una condición sea verdadera:

```python
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador
```

**⚠️ Cuidado:** Si la condición nunca se vuelve falsa, tendrás un bucle infinito.

---

## `break` - Salir del bucle

La palabra clave `break` termina el bucle inmediatamente:

```python
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)
# Imprime: 0, 1, 2, 3, 4
```

---

## `continue` - Saltar a la siguiente iteración

`continue` salta el resto del código en la iteración actual y pasa a la siguiente:

```python
for i in range(5):
    if i == 2:
        continue  # Salta cuando i es 2
    print(i)
# Imprime: 0, 1, 3, 4
```

---

## Bucles anidados

Puedes poner un bucle dentro de otro:

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

## Ejemplo práctico: Tabla de multiplicar

```python
numero = 5

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

---

## `else` con bucles

Python permite usar `else` con bucles. El bloque `else` se ejecuta cuando el bucle termina normalmente (no con `break`):

```python
for i in range(5):
    print(i)
else:
    print("Bucle completado sin interrupciones")

# Con break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Esto no se imprimirá")
```

---

## 💡 Ejercicios

1. Escribe un programa que imprima los números del 1 al 100.
2. Crea un programa que calcule la suma de todos los números del 1 al 100.
3. Escribe un programa que imprima los números pares del 1 al 20 usando `continue`.
4. Crea un programa que pida números al usuario hasta que ingrese 0, luego muestra la suma total (usa `while`).
5. Imprime un patrón de asteriscos:
   ```
   *
   **
   ***
   ****
   *****
   ```

---

**Siguiente:** [Ejercicios de Control de Flujo](03_ejercicios.md)
