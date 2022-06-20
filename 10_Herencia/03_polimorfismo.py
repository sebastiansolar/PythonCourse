

class Persona():
    def __init__(self):
        self.cedula = 12345
    def mensaje(self):
        print("Este mensaje viene de clase persona")

class Obrero(Persona):
    def __init__(self):
        self.especialista =1 

    def mensaje(self):
        print("Este mensaje viene de la clase obrero")

obrero_planta = Obrero()
#obrero_planta = Persona()
obrero_planta.mensaje()


class Gato():
    def hablar(self):
        print("Miau")

class Perro(Gato):
    def hablar(self):
        print("Guau")

def escucharMascotas(animal):
    animal.hablar()

miMascota = Perro()
escucharMascotas(miMascota)