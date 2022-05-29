

# def infinito(*args):
#     for args in args:
#         print(args)

# infinito(1,2,3,4,5, "Hola")

def infinito(**kwargs):   #Permite aplicarle una clave
    for kwarg in kwargs:
        print(kwarg, "----->", kwargs[kwarg])

infinito(a = "hola", b = 20, c = ["maria","pedro","Jose"])