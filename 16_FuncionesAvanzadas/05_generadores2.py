
from operator import ne


def devuelve_paises(*paises):
    for elemento in paises:
        yield from elemento

def devuelve_paises(*paises):
    yield from paises
    
paises_devuelta = devuelve_paises("Argentina", "Brasil", "Chile")
print(next(paises_devuelta))