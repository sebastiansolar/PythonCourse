

from tkinter.tix import InputOnly


i = input("Ingrese su nombre: ")
p = input("Ingresa el apellido: ")

print(f"El nombre de la persona es {i.upper()}")
print(f"El nombre de la persona es {p.lower()}")

print(f"EL nombre completo es {i.capitalize()} {p.capitalize()}")

print(f"El nombre aparece {i.count('Seba')} vez")
print(f"El nombre aparece en posicion {i.find('Seba')}")
print(f"El nombre aparece en posicion {i.isdigit()}")
print(f"El nombre aparece en posicion {i.split()}")

