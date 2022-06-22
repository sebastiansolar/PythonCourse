

def doblar(numero):
    return numero*2

numeros = [2,4,5,6,7,8]

i = map(doblar,numeros)
print(list(i))

for x in i:
    print(x)
    
lam = map(lambda x: x*2, numeros)
print(list(lam))





