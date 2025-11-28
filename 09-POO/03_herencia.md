# Herencia 👨‍👦

La **herencia** es un mecanismo que permite crear una nueva clase basada en una clase existente.

- **Clase Padre (Superclase)**: La clase original.
- **Clase Hija (Subclase)**: La nueva clase que hereda de la padre.

La clase hija hereda todos los atributos y métodos de la clase padre, y puede agregar los suyos propios o modificar los existentes.

## ¿Por qué usar herencia?

Permite reutilizar código. Si tienes una clase `Animal` con código para comer y dormir, no necesitas reescribirlo para `Perro` y `Gato`; simplemente haces que hereden de `Animal`.

## Sintaxis

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):  # Perro hereda de Animal
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):   # Gato hereda de Animal
    def hacer_sonido(self):
        return "¡Miau!"
```

## `super()`

La función `super()` permite llamar a métodos de la clase padre desde la clase hija. Es muy útil en el `__init__`.

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad) # Llama al __init__ de Persona
        self.curso = curso
```

---
[Volver al índice](README.md)
