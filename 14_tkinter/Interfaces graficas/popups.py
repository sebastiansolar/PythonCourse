from tkinter import *
from tkinter import messagebox

def salir():
    i = messagebox.askquestion("Salir","Estas seguro que desea salir?")
    if i == "yes":
        root.destroy()

def acerca():
    messagebox.showinfo("Informacion","Creado por Seba Stark")

def licencia():
    messagebox.showinfo("Licencia", "Producto licenciado por siempre")

def error():
    messagebox.showerror("Error","No se puede agregar nueva ventana")

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo")
archivoMenu.add_command(label="Nueva Ventana", command=error)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)


archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
archivoEditar.add_command(label="Deshacer")
archivoEditar.add_command(label="Rehacer")

archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de ...", command=acerca)
archivoAyuda.add_command(label="Menu", command=licencia)


root.mainloop()
