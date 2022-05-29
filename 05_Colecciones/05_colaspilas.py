
#FiFo  First input / First Output

from queue import Empty


cola = ['Jose','Martin','Bryan','Steve']

cola.append('Paola')
cola.append('Romina')

print(cola)
a = 0

i = cola.pop(a)
print(f"Estan atendiendo a {i}")


