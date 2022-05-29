
class Coche():
    def __init__(self):
        self.marca = "Audi"
        self.color = "Rojo"
        self.ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche se encuentra apagado"

    def __str__(self):
        return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.marca, self.color, self.ruedas)

miCoche = Coche()  #Instanciamos la clase
print(miCoche.arrancar(True))
print(str(miCoche))
