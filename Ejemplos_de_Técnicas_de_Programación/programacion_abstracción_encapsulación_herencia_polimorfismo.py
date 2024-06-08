# Abstracción
class Animal:
    def hacer_ruido(self):
        pass

# Encapsulación
class Perro(Animal):
    def hacer_ruido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_ruido(self):
        return "¡Miau!"

# Herencia
class AnimalDomestico:
    def __init__(self, nombre, animal):
        self.nombre = nombre
        self.animal = animal

    def presentarse(self):
        return f"¡Hola! Soy {self.nombre}, y mi mascota hace esto: {self.animal.hacer_ruido()}"

# Polimorfismo
perro = Perro()
gato = Gato()

mascota_perro = AnimalDomestico("Buddy", perro)
mascota_gato = AnimalDomestico("Whiskers", gato)

print(mascota_perro.presentarse())  # Output: ¡Hola! Soy Buddy, y mi mascota hace esto: ¡Guau!
print(mascota_gato.presentarse())   # Output: ¡Hola! Soy Whiskers, y mi mascota hace esto: ¡Miau!
