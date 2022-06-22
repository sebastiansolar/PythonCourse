from multiprocessing import context
import sqlite3

conexion = sqlite3.connect("PrimerBase.db") # Establecemos conexion

#conexion.close()

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))")
#conexion.close()

#cursor.execute("INSERT INTO USUARIOS VALUES('Brian',25,'Masculino')") # Insertar elementos


# cursor.execute("SELECT * FROM USUARIOS")
# usuario = cursor.fetchone()
# print(usuario) #usuario[0]

# usuarios = [
#     ('Brian', 25, 'Masculino'),
#     ('Stark', 35, 'Masculino'),
#     ('Tchalla', 27, 'Masculino'),   
# ]
# cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)",usuarios)

cursor.execute("SELECT * FROM USUARIOS")
usuarios = cursor.fetchall()
print(usuarios)

for i in usuarios:
    print(i)


conexion.commit()
conexion.close()