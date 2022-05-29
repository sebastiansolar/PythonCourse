

class Coche():
    def __init__(self, marca, km, year):
        self.marca = marca
        self.__km = 200
        self.year = year
        print(f'Se ha creado un auto {self.marca}')
    
    def __del__(self):
        print(f'Se ha vendido el auto {self.marca}')
    
    def __str__(self):
        return f'El auto es un {self.marca}, tiene {self.__km}, y es del anio {self.year}'

miCoche = Coche("Audi", 100, 1995)
print(str(miCoche))

# del(miCoche)

print(25*'***')