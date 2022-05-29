# Clases y objetos

class Gelatina:
    def __init__(self, sabor, color, size):
        self.sabor = sabor
        self.color = color
        self.size = size
    
    def imprimir(self):
        print(f"La gelatina es de {self.sabor}")
        print(f"La gelatina se ve de {self.color}")
        print(f"La gelatina es {self.size}")

gel1 = Gelatina("Roja", "Frutilla", "Grande")
gel2 = Gelatina("Amarilla", "Pineapple", "Grande")
gel3 = Gelatina("Verde", "Manzana", "Grande")
gel4 = Gelatina("Azul", "Berries", "Grande")

gel1.imprimir()



class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def datosPersonales(self):
        print("El nombre de la persona es ", self.nombre)
        print("La edad de la persona es ", self.edad)
        print("El sexo de la persona es ", self.sexo)

miPersona = Persona("Seba", 25, "Masculino")
miPersona2 = Persona("Ainoa", 26, "Femenino")
miPersona3 = Persona("Aitana", 26, "Femenino")

miPersona.datosPersonales()
miPersona2.datosPersonales()
miPersona3.datosPersonales()

