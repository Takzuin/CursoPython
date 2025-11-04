"""
Ejemplo: Variables y tipos de datos
===================================
"""

# Números enteros (int)
edad = 25
cantidad = 100
print(f"Edad: {edad}, tipo: {type(edad)}")

# Números decimales (float)
precio = 19.99
temperatura = -5.5
print(f"Precio: {precio}, tipo: {type(precio)}")

# Cadenas de texto (str)
nombre = "Ana"
ciudad = 'Madrid'
print(f"Nombre: {nombre}, tipo: {type(nombre)}")

# Booleanos (bool)
es_estudiante = True
tiene_coche = False
print(f"Es estudiante: {es_estudiante}, tipo: {type(es_estudiante)}")

# Operaciones básicas
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5
potencia = 2 ** 3

print(f"\nOperaciones matemáticas:")
print(f"10 + 5 = {suma}")
print(f"10 - 5 = {resta}")
print(f"10 * 5 = {multiplicacion}")
print(f"10 / 5 = {division}")
print(f"2 ** 3 = {potencia}")

# Concatenación de cadenas
saludo = "Hola, " + nombre + "!"
print(f"\n{saludo}")
