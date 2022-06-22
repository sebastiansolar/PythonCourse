
# Forma tradicional

def suma(x,y):
    return (x+y)

print(suma(2,5))

# Utilizando lambda

i = lambda x,y: x+y
print(i(2,3))


# Ejemplos
impar = lambda numero: numero%2 != 0
print(impar(4))

revertir = lambda cadena: cadena[::-1]
print(revertir("Python"))

doblar = lambda numero: numero*2
print(doblar(2))