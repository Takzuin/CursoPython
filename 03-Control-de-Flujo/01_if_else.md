# Sentencias Condicionales en Python 🚦

Las sentencias condicionales te permiten tomar decisiones en tu código. Python ejecutará diferentes bloques de código dependiendo de si una condición es verdadera o falsa.

---

## La sentencia `if`

La forma más básica de control de flujo es la sentencia `if`:

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

**Importante:** Python usa **indentación** (espacios o tabulaciones) para definir bloques de código. Todo lo que esté indentado después del `if` se ejecutará solo si la condición es verdadera.

---

## La sentencia `else`

Si quieres ejecutar código cuando la condición es falsa, usa `else`:

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

---

## La sentencia `elif`

Cuando necesitas verificar múltiples condiciones, usa `elif` (abreviatura de "else if"):

```python
nota = 85

if nota >= 90:
    print("¡Excelente! Calificación: A")
elif nota >= 80:
    print("Muy bien. Calificación: B")
elif nota >= 70:
    print("Bien. Calificación: C")
elif nota >= 60:
    print("Aprobado. Calificación: D")
else:
    print("Reprobado. Calificación: F")
```

---

## Operadores de comparación

Para crear condiciones, usamos operadores de comparación:

| Operador | Significado |
|----------|-------------|
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual que |
| `<=` | Menor o igual que |

---

## Operadores lógicos

Puedes combinar condiciones con operadores lógicos:

- **`and`**: Ambas condiciones deben ser verdaderas
- **`or`**: Al menos una condición debe ser verdadera
- **`not`**: Invierte el valor de la condición

```python
edad = 20
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Puedes entrar")

if edad < 18 or not tiene_permiso:
    print("No puedes entrar")
```

---

## Ejemplo práctico: Calculadora simple

```python
numero1 = 10
numero2 = 5
operacion = "+"

if operacion == "+":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")
    else:
        print("Error: No se puede dividir por cero")
else:
    print("Operación no válida")
```

---

## 💡 Ejercicios

1. Escribe un programa que determine si un número es positivo, negativo o cero.
2. Crea un programa que verifique si un año es bisiesto (divisible por 4, excepto los siglos que no son divisibles por 400).
3. Escribe un programa que pida la temperatura y sugiera qué ropa usar (frío < 15°C, templado 15-25°C, calor > 25°C).

---

**Siguiente:** [Bucles en Python](02_loops.md)
