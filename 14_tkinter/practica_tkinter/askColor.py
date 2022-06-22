from logging import root
import tkinter as tk
from tkinter.colorchooser import askcolor
from turtle import title

root = tk.Tk()
root.title('Tkinter Color')
root.geometry('300x50')


def cambiarColor():
    colores = askcolor(title="Tkinter colores")
    root.config(bg=colores[1])
    
tk.Button(
    root,
    text='Cambiar color',
    command=cambiarColor
).pack(expand=True)



root.mainloop()