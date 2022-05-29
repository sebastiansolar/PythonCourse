
try:

    c = int(input("Ingrese un valor: "))
    c/0

except ValueError:
    print("Error, no se puede sumar una cadena de texto")  
except Exception as c:
    print(type(c).__name__)