# Estructuras que extraen valores de una funcion y lo guardan en objetos iterables


def generaPares(limite):
    num=1
    miLista=[]
    while num<=limite:
        miLista.append(num*2)
        num += 1
    return miLista
print(generaPares(6))


def generaPares2(limite):
    num=1
    while num<=limite:
        yield num * 2
        num += 1

devuelvePares = generaPares2(10)
print(next(devuelvePares))
print("Otra linea")
print(next(devuelvePares))