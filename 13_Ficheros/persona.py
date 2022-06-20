import pickle
from io import open

class Persona:

    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def caracteristicas(self):
        print(f"El nombre es: {self.nombre}")
        print(f"El apellido es: {self.apellido}")
        print(f"La edad es: {self.edad}")
        print(f"El sexo es: {self.sexo}")

miPersona1 = Persona("Tony","Stark",52,"Masculino")
miPersona2 = Persona("Brad","Stark",32,"Masculino")
miPersona3 = Persona("Alexander","Stark",22,"Masculino")

listaPersona = [miPersona1,miPersona2,miPersona3]

fichero = open("Personas", "wb")
pickle.dump(listaPersona, fichero)
fichero.close()

ficheroleer = open("Personas", "rb")
lista = pickle.load(ficheroleer)
for i in lista:
    print(i.caracteristicas())

ficheroleer.close()