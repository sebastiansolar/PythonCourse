from io import open

# ---- Creando Fichero ------

fichero = open("archivo2.txt","w")

texto = "Hola, estamos trabajando con python, viendo los cursores"
fichero.write(texto)
fichero.close()

# Mover cursor

fichero = open("archivo2.txt","r")
#fichero.seek(13)
#print(fichero.read(5))
print(fichero.read())
fichero.close()

#  --- Dejarlo al medio  ---

fichero = open("archivo2.txt","r")
fichero.seek(len(fichero.read())/2)
print(fichero.read())
fichero.close()

# --- Que se situe en la primera linea

fichero = open("archivo2.txt","w")
fichero.write("Hola")
#fichero.seek(len(fichero.readline()))
fichero = open("archivo2.txt","r+")
print(fichero.readlines())
fichero.close()




