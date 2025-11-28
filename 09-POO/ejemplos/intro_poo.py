# Ejemplo de Programación Orientada a Objetos

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} arrancado."
        else:
            return "El vehículo ya está encendido."

    def detener(self):
        if self.encendido:
            self.encendido = False
            return f"{self.marca} {self.modelo} detenido."
        else:
            return "El vehículo ya está detenido."

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def abrir_maletero(self):
        return "Abriendo maletero..."

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def hacer_caballito(self):
        return "¡Haciendo un caballito!"

# Probando el código
if __name__ == "__main__":
    print("--- Coche ---")
    mi_coche = Coche("Toyota", "Corolla", 4)
    print(mi_coche.arrancar())
    print(mi_coche.abrir_maletero())
    print(mi_coche.detener())

    print("\n--- Moto ---")
    mi_moto = Moto("Yamaha", "MT-07")
    print(mi_moto.arrancar())
    print(mi_moto.hacer_caballito())
