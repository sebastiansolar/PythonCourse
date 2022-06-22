import sqlite3

conexion = sqlite3.connect("Productos.db")

cursor = conexion.cursor()

# Leer
cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P = 'Panaderia'")
productos = cursor.fetchall()
print(productos)

# Actualizar
cursor.execute("UPDATE PRODUCTOS SET SECCION_P='PANADERIA' WHERE SECCION_P = 'Panaderia'")

# Eliminar
cursor.execute("DELETE FROM PRODUCTOS WHERE SECCION_P = 'Carniceria'")

conexion.commit()
conexion.close()