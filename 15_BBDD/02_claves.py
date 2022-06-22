from itertools import product
import sqlite3

conexion = sqlite3.connect("Productos.db")

cursor = conexion.cursor()

# cursor.execute('''
#                CREATE TABLE PRODUCTOS(
#                    CODIGO_P VARCHAR(10)PRIMARY KEY,
#                    NOMBRE_P VARCHAR(20),
#                    SECCION_P VARCHAR(20)
#                )
               
#                ''')

cursor.execute('''
               CREATE TABLE PRODUCTOS(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NOMBRE_P VARCHAR(20),
                   PRECIO_P INTEGER,
                   SECCION_P VARCHAR(20)
               )
               
               ''')


productos = [
    ('Leche', 2000,'Lacteos'),
    ('Marraqueta', 1600, 'Panaderia'),
    ('Asado', 6700, 'Carniceria')
    ]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)
#cursor.execute("INSERT INTO PRODUCTOS VALUES('AR4','Pan', 'Panaderia')")

conexion.commit()
conexion.close()
