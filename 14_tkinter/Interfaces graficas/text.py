from cProfile import label
from tkinter import *

root = Tk()


texto = Text(root)
texto.pack()
texto.config(width=40,height=15,padx=15,pady=15,selectbackground="blue")

label = Label(root, text="Escribe aqui")
label.pack()
label.config(bg="red", font="Curier, 20")

root.mainloop()