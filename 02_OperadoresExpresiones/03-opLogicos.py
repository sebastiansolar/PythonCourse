# Operador not

print(not True)
print(not False)

# Operador and

print(True and False)  # Falso
print(True and True)   # Verdadero
print(False and False) # Verdadero

# Operador or

print(True or False)  # Verdadero
print(False or True)  # Verdadero
print(True or True)   # Verdadero
print(False or False) # Falso


c = "Python"
largoPalabra = len(c)
print(largoPalabra)

print(len(c) < 8 and c[0] == "F") # Falso
print(len(c) < 8 or c[0] == "F")  # Verdadero


print("---- Sistema de becas ----")

km = int(input("A cuantos km vives de la U ? "))
hermanos = int(input("Cuantos hermanos tienes ? "))
ingreso = int(input("De cuanto es el ingreso de tu hogar ? "))

if km > 10 and hermanos < 2 and ingreso > 2000:
    print("Tienes derecho")
else:
    print("No tienes derecho")