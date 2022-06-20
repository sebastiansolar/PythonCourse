from PaquetePersona import datos_persona
from datos_persona import Persona

class Empleado(Persona):
    def datosEmpleado(self, vacaciones, salario):
        print(f"sus dias de vacaciones son {vacaciones}")
        print(f"sus salario es {salario}")