from logging.handlers import RotatingFileHandler
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def seleccionar(opcion):
    print(opcion)
    
ttk.Button(root, text="Python", command=lambda:("Python")).pack()
ttk.Button(root, text="Java", command=lambda:("Java")).pack()
ttk.Button(root, text="JavaScript", command=lambda:("JavaScript")).pack()



root.mainloop()