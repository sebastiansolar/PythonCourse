import imp
from tkinter import *

root = Tk()
root.config(bd=20, bg="goldenrod3")
root.title("Casa de comidas")


def orden():
    lista=""
    if(queso.get()):
        lista += " Con queso"
    else:
        lista += " Sin queso"
    if(lechuga.get()):
        lista += " Con lechuga"
    else:
        lista += " Sin lechuga"
    imprimir.config(text=lista)


queso = IntVar()
lechuga = IntVar()

imagen = PhotoImage("200.gif")
Label(root,image=imagen).pack()

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")

Label(frame, text="Como quieres tu burger ?", bg="goldenrod3", font="Curier 15").pack(anchor="w")

Checkbutton(frame, text="Con queso", variable=queso, onvalue=1, offvalue=0, font="Curier 10", bg="goldenrod3",command=orden).pack(anchor="w")

Checkbutton(frame, text="Con Lechuga", variable=lechuga, onvalue=1, offvalue=0, font="Curier 10", bg="goldenrod3", command=orden).pack(anchor="w")

imprimir = Label(frame, bg="goldenrod3")
imprimir.pack()

root.mainloop()