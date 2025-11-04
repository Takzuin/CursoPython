"""
Ejemplo: Funciones en Python
============================
"""

# --- FUNCIÓN BÁSICA ---
def saludar():
    """Función simple que imprime un saludo."""
    print("¡Hola desde una función!")

saludar()

# --- FUNCIÓN CON PARÁMETROS ---
def saludar_persona(nombre):
    """Saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Carlos")

# --- FUNCIÓN CON RETORNO ---
def sumar(a, b):
    """Suma dos números y retorna el resultado."""
    return a + b

resultado = sumar(5, 3)
print(f"\n5 + 3 = {resultado}")

# --- FUNCIÓN CON VALORES POR DEFECTO ---
def presentar(nombre, edad=18, ciudad="Madrid"):
    """Presenta a una persona con información opcional."""
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

print()
presentar("María")
presentar("Juan", 25)
presentar("Ana", 30, "Barcelona")

# --- FUNCIÓN CON *ARGS ---
def sumar_todos(*numeros):
    """Suma cualquier cantidad de números."""
    total = sum(numeros)
    return total

print(f"\nSuma de 1, 2, 3: {sumar_todos(1, 2, 3)}")
print(f"Suma de 10, 20, 30, 40: {sumar_todos(10, 20, 30, 40)}")

# --- FUNCIÓN LAMBDA ---
cuadrado = lambda x: x ** 2
print(f"\nCuadrado de 5: {cuadrado(5)}")

# Usar lambda con map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrados de {numeros}: {cuadrados}")

# --- FUNCIÓN RECURSIVA ---
def factorial(n):
    """Calcula el factorial de n recursivamente."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"\nFactorial de 5: {factorial(5)}")

# --- DOCUMENTACIÓN DE FUNCIONES ---
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

area = calcular_area_rectangulo(5, 3)
print(f"\nÁrea de rectángulo (5x3): {area}")

# Ver la documentación
print("\nDocumentación de la función:")
print(calcular_area_rectangulo.__doc__)
