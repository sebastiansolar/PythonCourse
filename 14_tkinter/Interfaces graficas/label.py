from re import T
from tkinter import *
from turtle import color

root = Tk()

imagen = PhotoImage(file="200.gif")

texto_nuevo = StringVar()
texto_nuevo.set("Python")

root.title("Bienvenido")
root.config(width=400,height=350)

label = Label(root,text="Hola Mundo")
label.place(x=50,y=100)
label.config(bg="blue", fg="white", font="Curier, 20")

label2 = Label(root,text="Bienvenidos")
label2.place(x=100,y=50)
label2.config(textvariable=texto_nuevo)

label3 = Label(root, image=imagen)
#label3.place(x=150,y=150)
label3.pack()

root.mainloop()