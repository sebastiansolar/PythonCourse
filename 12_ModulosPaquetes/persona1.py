import sys 
sys.path.append(r'C:\Users\Sebastian\Desktop\Python\12_ModulosPaquetes\PaquetePersona')

from PaquetePersona.datos_persona import *
from PaquetePersona.empleado import *

miPersona1 = Persona("Seba","Stark",25,"Masculino")
miEmpleado1 = Empleado(miPersona1.nombre, miPersona1.apellido, miPersona1.edad, miPersona1.sexo)

miEmpleado1.datosEmpleado(22,25000)
