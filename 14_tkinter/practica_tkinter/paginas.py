from telnetlib import EXOPL
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x300')
root.title('Paginas')

# cuadro madre

cuadroMadre = ttk.Notebook(root)
cuadroMadre.pack(pady=10, expand=True)

frame1 = ttk.Frame(cuadroMadre, width=400,height=280)
frame2 = ttk.Frame(cuadroMadre, width=400,height=280)

frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

# Agregamos los frames a nuestro cuadro madre

cuadroMadre.add(frame1, text="Informacion General")
cuadroMadre.add(frame2, text="Perfil")

root.mainloop()