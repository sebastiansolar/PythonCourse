from logging import root
import tkinter as tk
from tkinter import Button, ttk


root = tk.Tk()
root.title('Barra de progreso')
root.geometry('300x50')

root.grid()

bd = ttk.Progressbar(
    root,
    orient="horizontal",
    mode="indeterminate",
    length=280
)

bd.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

boton_iniciar = Button(
    root, text='iniciar', command=bd.start
)
boton_iniciar.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=tk.E)

boton_parar = Button(
    root, text='parar', command=bd.stop
)
boton_parar.grid(column=1, row=1, columnspan=2, padx=10, pady=10, sticky= tk.W)




root.mainloop()