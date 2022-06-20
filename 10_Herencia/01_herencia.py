
class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    
    def datosPersonales(self):
        print(f"El nombre de la persona es {self.nombre}")
        print(f"El apellido de la persona es {self.apellido}")
        print(f"La edad de la persona es {self.edad}")
        print(f"El sexo de la persona es {self.sexo}")

miPersona = Persona("Seba","Stark",25,"Masculino")
miPersona.datosPersonales()

class Empleado(Persona):

    def datosEmpleado(self, vacaciones, salario):
        print(f"Sus dias de vacaciones son: {vacaciones}")
        print(f"Su salario es:  {salario}")

miPersona2 = Empleado("Bran", "Stark", 22, "Masculino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(12,50000)