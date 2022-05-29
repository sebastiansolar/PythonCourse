import sys
print(sys.argv)

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error: Introdujo uno o mas de dos argumentos")
    print("Solucion: Introduce los argumentos correctamente")
    print("Solucion ejemplo: entrada_argumentos.py 'text' 10")