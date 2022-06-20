from io import open

# -------- Escritura archivo -------------

# fichero = open("archivo.txt","w") #Creacion y apertura
# texto = "Hola mundo\n Estudio Python"
# fichero.write(texto) # Manipulacion
# fichero.close()

# -------- Lectura de archivo ------------

fichero = open("archivo.txt","r")
texto = fichero.read()
fichero.close()
print(texto)

# ------- Lectura por lineas en lista --------

fichero = open("archivo.txt","r")
linea = fichero.readlines()
fichero.close()
print(linea)

# ------- Append agregar a fichero ----------

fichero = open("archivo.txt","a")
lineaNueva = "\nProbando el metodo append"
fichero.write(lineaNueva)
fichero.close()
print(fichero)