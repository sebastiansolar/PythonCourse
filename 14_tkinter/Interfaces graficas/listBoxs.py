from cgitb import text
from importlib.metadata import entry_points
from itertools import product
from tkinter import *

root = Tk()
root.geometry("400x400")

productos = Label(root, text="Productos")
productos.pack()

def agregar():
    listaProductos.insert(END, entrada.get())

listaProductos = Listbox(root, width=50)
listaProductos.insert(0,"Carne")
listaProductos.insert(1,"Pollo")
listaProductos.insert(2,"Verdura")
listaProductos.insert(3,"Fruta")
listaProductos.pack()

#Eliminar productos

listaProductos.delete(0)

entrada = Entry(root, bd=10)
entrada.pack()

boton = Button(root, text="Agregar producto", command=agregar)
boton.pack()

root.mainloop()

