

set_conjunto1 = set({1,2,3,4})
set_conjunto2 = set({1.0,"Auto",True})
set_conjunto3 = set_conjunto2.copy()
set_conjunto1.add(22)  #Agregar
print(set_conjunto1)
print(set_conjunto3)



################ Discard ##########################

set_conjunto1.discard(1)
print(set_conjunto1)

############### Remove ############################

set_conjunto1.remove(2)
print(set_conjunto1)