#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia #y Lengua) en una lista y la muestre por pantalla.

materias = ["Matematicas","Fisica", "Quimica", "Historia", "Lenguaje"]

print("El alumno tiene las siguientes materias: ")
for x in materias:
    print(f"{x}")


# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

materias = ["Matematicas","Fisica", "Quimica", "Historia", "Lenguaje"]

count = 0
for x in materias:
    print(f"Yo estudio {materias[count]}")
    count += 1

#  Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

materias = ["Matematicas","Fisica", "Quimica", "Historia", "Lenguaje"]

count = 0
notas = []
for x in materias:
    notas.append(input(f"Que nota sacaste en {materias[count]}?: "))
    count += 1

count2 = 0
for x in materias:
    print(f"Obtuviste una nota {notas[count2]} en {materias[count2]} ")
    count2 += 1