
#Conjunto - Colección desordenada de elementos, Inmutable. 

mi_conjunto = {1.0,1,2,3,"Hola", (1,2,3)}
print(mi_conjunto)
print(type(mi_conjunto))

mi_conjunto2 = set() #Vacio

mi_conjunto2.add("asd") #Agrega elemento
mi_conjunto2.update([1,2,3]) #Actualiza solo lo que no se encuentra
mi_conjunto2.discard(2) #Si no lo encuentra lo deja tal cual
mi_conjunto2.remove(3)  #Si no lo encuentra arroja un error
mi_conjunto.clear()  #Elimina todo

print(mi_conjunto2)
