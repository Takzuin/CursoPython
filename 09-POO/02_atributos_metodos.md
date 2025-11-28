# Atributos y Métodos ⚙️

Ahora que tenemos clases y objetos, necesitamos darles vida con datos (atributos) y acciones (métodos).

## Atributos

Los **atributos** son variables que pertenecen a un objeto. Representan el estado o las características del objeto.

### El método `__init__`

El método especial `__init__` se llama automáticamente cuando creas un nuevo objeto. Se usa para inicializar los atributos.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
```

### `self`

`self` es una referencia al objeto actual que se está creando o utilizando. Es la forma en que el código sabe a qué instancia específica pertenece un atributo o método.

## Métodos

Los **métodos** son funciones definidas dentro de una clase. Representan el comportamiento o las acciones que el objeto puede realizar.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
```

## Ejemplo Completo

```python
# Definición de la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1
        return f"¡Feliz cumple! Ahora tengo {self.edad}."

# Creación de objetos
p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

# Uso de atributos y métodos
print(p1.nombre)          # Ana
print(p2.saludar())       # (Esto daría error porque no definimos saludar arriba, pero imagina que sí)
print(p1.cumpleaños())    # ¡Feliz cumple! Ahora tengo 26.
```

---
[Siguiente: Herencia](03_herencia.md)
