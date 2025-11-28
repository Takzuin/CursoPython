# Módulo 09: Programación Orientada a Objetos (POO) 🏗️

¡Bienvenido al noveno módulo! 🎉

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que utiliza "objetos" para modelar datos y comportamientos del mundo real. Es fundamental para construir aplicaciones complejas y escalables.

---

## 📚 ¿Qué aprenderás en este módulo?

- **Clases y Objetos**: Los bloques fundamentales de la POO.
- **Atributos y Métodos**: Cómo dar estado y comportamiento a tus objetos.
- **El constructor `__init__`**: Inicializando objetos.
- **`self`**: Entendiendo la referencia al objeto actual.
- **Herencia**: Reutilizando código y creando jerarquías.

---

## 🛠 Contenido del módulo

1. [Clases y Objetos](01_clases_y_objetos.md): Entiende la diferencia entre el plano y la casa.
2. [Atributos y Métodos](02_atributos_metodos.md): Define las características y acciones.
3. [Herencia](03_herencia.md): Extiende la funcionalidad de tus clases.

---

## 💡 ¿Por qué usar POO?

La POO te permite:
- ✅ **Organizar código complejo**: Agrupa datos y lógica relacionada.
- ✅ **Reutilizar código**: Evita la duplicación mediante la herencia.
- ✅ **Modelar el mundo real**: Representa entidades como usuarios, productos, etc.
- ✅ **Modularidad**: Facilita el mantenimiento y la colaboración.

---

## 🚀 Ejemplo rápido

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Crear un objeto
mi_perro = Perro("Firulais")
print(mi_perro.ladrar())
```

---

¡Vamos a construir objetos increíbles! 🚀
