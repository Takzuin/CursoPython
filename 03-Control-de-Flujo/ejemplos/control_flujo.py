"""
Ejemplo: Condicionales y bucles
===============================
"""

# --- CONDICIONALES ---
print("=== Ejemplo de condicionales ===")
edad = 20

if edad >= 18:
    print(f"Edad {edad}: Eres mayor de edad")
else:
    print(f"Edad {edad}: Eres menor de edad")

# Múltiples condiciones
nota = 85

if nota >= 90:
    print(f"Nota {nota}: ¡Excelente!")
elif nota >= 70:
    print(f"Nota {nota}: Bien")
elif nota >= 50:
    print(f"Nota {nota}: Aprobado")
else:
    print(f"Nota {nota}: Reprobado")

# --- BUCLES FOR ---
print("\n=== Ejemplo de bucle for ===")
print("Contando del 1 al 5:")
for i in range(1, 6):
    print(i, end=" ")

print("\n\nIterar sobre una lista:")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"- {fruta}")

# --- BUCLES WHILE ---
print("\n=== Ejemplo de bucle while ===")
contador = 0
print("Contando hasta 5:")
while contador < 5:
    contador += 1
    print(contador, end=" ")

# --- BREAK Y CONTINUE ---
print("\n\n=== Ejemplo de break ===")
for i in range(10):
    if i == 5:
        print(f"¡Encontré el 5! Saliendo del bucle...")
        break
    print(i, end=" ")

print("\n\n=== Ejemplo de continue ===")
print("Números impares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:  # Si es par, salta esta iteración
        continue
    print(i, end=" ")

print("\n")
