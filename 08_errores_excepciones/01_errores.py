

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion no valida"

op1 = int(input("Ingrese el numero 1: "))
op2 = int(input("Ingrese el numero 2: "))

operacion = input("Introduce la operacion a realizar (suma, resta, multiplicar, dividir)")

if operacion == "suma":
    print(suma(op1,op2))

elif operacion == "resta":
    print(resta(op1,op2))

elif operacion == "multiplicar":
    print(multiplicar(op1,op2))

else:
    print(dividir(op1,op2))

print("Ejecutando")   