

diccionario = {
    "clave1": 123,
    'clave2': True,
    'clave3': [1,2,3,4]
}

print(type(diccionario['clave1']))
print(type(diccionario['clave2']))
print(type(diccionario['clave3']))

#### Para saber las claves ####

print(diccionario.keys())

#### y para los valores ######

print(diccionario.values())

#### Ambas Cosas #############

print(diccionario.items())

for i,c in diccionario.items():
    print(f'Clave : {i}, Valor: {c}')