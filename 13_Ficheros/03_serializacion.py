import pickle
from io import open

lista = ["Maria", "Pedro", "Jose", "Antonio"]

fichero = open("lista_nombres","wb") #write binarie
pickle.dump(lista,fichero)  #De esta forma guardamos en binario

fichero.close()

#Ahora queremos ver que es lo que tenemos

fichero = open("lista_nombres", "rb") #Read binarie
lista2 = pickle.load(fichero)
fichero.close()
print(lista2)