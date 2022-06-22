

def saludar(arg):
    """Funcion para saludar

    Args:
        arg (string): mensaje que se usara para saludar
    """
    print("Hola ", arg)
    
class Persona:
    """Aqui creamos la Persona
    """
    def __init__(self,):
        """Inicializamos las caracteristicas de la persona
        """
        pass
    def estado(self):
        """Consultamos el estado de la persona
        """
        pass
    
help(Persona)


#Pydoc
#python -m pydoc docs #Muestra documentacion en consola
#python-m pydoc -w docs #Genera un html con documentacion