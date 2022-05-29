# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo():
    print("Hola amiga!")

saludo()

# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saludo_name(nombre):
    return f"Hola {nombre}"

print(saludo_name("Seba"))

# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    
    i = numero
    facto = 1
    for x in range (1, i + 1):
        facto = facto * x
    return facto

print(factorial(23))
