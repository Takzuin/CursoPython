# 2. Tipos de Datos en Python 🧮

En Python, los **tipos de datos** son fundamentales para entender cómo manipular la información en tu programa. 
Cada variable que declaras tiene un tipo específico, que define qué tipo de valor puede almacenar y cómo se comporta.

---

## 📝 Tipos de Datos Básicos

### 1. **Enteros (int)**
Los enteros son números sin decimales. Pueden ser positivos o negativos.

Ejemplo:
```python
edad = 25
contador = -10

2. Flotantes (float)

Los flotantes son números que tienen decimales.

Ejemplo:

altura = 1.75
temperatura = -5.4

3. Cadenas de texto (str)

Las cadenas de texto, o strings, son secuencias de caracteres que puedes usar para almacenar palabras, frases o cualquier texto.

Ejemplo:

nombre = "Juan"
mensaje = "Hola, Python"

Las cadenas de texto se pueden definir con comillas dobles (") o comillas simples (').
4. Booleanos (bool)

Los valores booleanos solo pueden ser True (verdadero) o False (falso). Son muy útiles para tomar decisiones en los programas.

Ejemplo:

es_adulto = True
es_vegetariano = False

⚙️ Operaciones con Tipos de Datos

Python te permite realizar operaciones matemáticas con los tipos de datos adecuados. Por ejemplo:
Operaciones con enteros y flotantes:

# Suma de enteros
suma = 5 + 3  # Resultado: 8

# Suma de flotantes
suma_float = 5.5 + 3.2  # Resultado: 8.7

# Dividir un entero entre un flotante
division = 10 / 3  # Resultado: 3.333...

Operaciones con cadenas:

Las cadenas de texto pueden ser concatenadas (unidas) usando el operador +:

nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido  # Resultado: "Juan Pérez"

También puedes multiplicar cadenas por un número:

saludo = "¡Hola! " * 3  # Resultado: "¡Hola! ¡Hola! ¡Hola! "

Operaciones con booleanos:

Los valores booleanos se pueden usar en operaciones lógicas, como en las comparaciones:

a = 5
b = 10
resultado = a < b  # Resultado: True

⚠️ Convertir entre Tipos de Datos

En Python, puedes convertir un tipo de dato a otro utilizando funciones de conversión. Aquí te mostramos algunas:

    Convertir a entero (int):

numero = int("5")  # Convierte la cadena "5" en un número entero 5

    Convertir a flotante (float):

numero = float("3.14")  # Convierte la cadena "3.14" en un número flotante 3.14

    Convertir a cadena (str):

numero = str(25)  # Convierte el número 25 en la cadena "25"

✍️ Desafío

Crea variables de diferentes tipos de datos y realiza operaciones con ellas. Luego, imprime el resultado en la pantalla.

Ejemplo:

numero1 = 10
numero2 = 5.5
nombre = "Python"
es_verdadero = True

resultado = numero1 + numero2
mensaje = "El resultado es " + str(resultado)

print(mensaje)

💡 Consejos

    Presta atención al tipo de dato: Al trabajar con variables, es importante saber qué tipo de dato estás utilizando. 
    Algunas operaciones solo funcionan con ciertos tipos (por ejemplo, no puedes sumar una cadena de texto con un número sin hacer una conversión adecuada).

    Usa las funciones de conversión: Si necesitas cambiar de un tipo de dato a otro, recuerda que Python tiene funciones como int(), float(), y str() para ayudarte.

¡Ahora que entiendes los tipos de datos básicos en Python, puedes comenzar a trabajar con diferentes tipos de información y realizar operaciones con ellos! Practica 
manipulando variables de diferentes tipos y experimenta con las conversiones entre ellos.


---

Este archivo proporciona una explicación sobre los tipos de datos básicos en Python y cómo usarlos correctamente, con ejemplos y ejercicios. Si necesitas algún ajuste o más detalles, ¡dímelo! 😊

