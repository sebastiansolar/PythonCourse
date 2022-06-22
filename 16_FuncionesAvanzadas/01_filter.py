
edades = [19,42,23,43,18,35,64,5,14,16]


def mayores(edad):
    return edad >=18

def menores(edad):
    return edad < 18

entrar = list(filter(mayores,edades))
noEntra = list(filter(menores, edades))

print(entrar)
print(noEntra)

