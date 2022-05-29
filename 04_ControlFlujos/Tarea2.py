
#1 Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#2 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "passTest"

pass_user = str(input("Ingrese la password: "))
permitido = False

while not permitido:
    if pass_user.upper() == password.upper():
        print("Correcto")
        permitido = True
    else:
        print("Incorrecto, pruebe otra vez")
        pass_user = str(input("Ingrese la password: "))

#3 Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero_1 = int(input("Ingresa el numero 1: "))
numero_2 = int(input("Ingresa el numero 2: "))

if numero_2 == 0:
    print("Error")
else:
    print(f"La división entre {numero_1} y {numero_2} es {numero_1/numero_2}")