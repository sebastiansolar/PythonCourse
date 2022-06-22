from tkinter import *

i = 0

def click(valor):
    global i
    entrada.insert(i,valor)
    i += 1

def borrar():
    entrada.delete(0, END)
    i = 0

def operaciones():
    operacion = entrada.get()
    resultado = eval(operacion)
    entrada.delete(0, END)
    entrada.insert(0, resultado)
    i = 0



root = Tk()
root.title("Calculadora")


# Entrada

entrada = Entry(root, font="Curier 20")
entrada.grid(row=0, column=0, columnspan=4, padx=40, pady=5)

#Botones

btn1 = Button(root, text="1", width=5, height=2, command=lambda:click(1))
btn2 = Button(root, text="2", width=5, height=2, command=lambda:click(2))
btn3 = Button(root, text="3", width=5, height=2, command=lambda:click(3))
btn4 = Button(root, text="4", width=5, height=2, command=lambda:click(4))
btn5 = Button(root, text="5", width=5, height=2, command=lambda:click(5))
btn6 = Button(root, text="6", width=5, height=2, command=lambda:click(6))
btn7 = Button(root, text="7", width=5, height=2, command=lambda:click(7))
btn8 = Button(root, text="8", width=5, height=2, command=lambda:click(8))
btn9 = Button(root, text="9", width=5, height=2, command=lambda:click(9))
btn0 = Button(root, text="0", width=10, height=2,command=lambda:click(0))

btnpare1 = Button(root, text="(", width=5, height=2, command=lambda:click("(") )
btnpare2 = Button(root, text=")", width=5, height=2, command=lambda:click(")") )
btndot = Button(root, text=".", width=5, height=2, command=lambda:click(".") )
btnequal = Button(root, text="=", width=5, height=2, command=lambda:operaciones())
btn_del = Button(root, text="DEL", width=5, height=2, command=lambda:borrar())

btn_div = Button(root, text="/", width=5,height=2, command=lambda:click("/"))
btn_multi = Button(root, text="*", width=5,height=2, command=lambda:click("*"))
btn_suma = Button(root, text="+", width=5,height=2, command=lambda:click("+"))
btn_resta = Button(root, text="-", width=5,height=2, command=lambda:click("-"))

# Colocar botones

btn_del.grid(row=1,column=0,padx=5, pady=5)
btnpare1.grid(row=1,column=1,padx=5, pady=5)
btnpare2.grid(row=1,column=2,padx=5, pady=5)
btn_div.grid(row=1,column=3,padx=5, pady=5)

btn7.grid(row=2,column=0,padx=5, pady=5)
btn8.grid(row=2,column=1,padx=5, pady=5)
btn9.grid(row=2,column=2,padx=5, pady=5)
btn_multi.grid(row=2,column=3,padx=5, pady=5)

btn4.grid(row=3,column=0,padx=5, pady=5)
btn5.grid(row=3,column=1,padx=5, pady=5)
btn6.grid(row=3,column=2,padx=5, pady=5)
btn_suma.grid(row=3,column=3,padx=5, pady=5)

btn1.grid(row=4,column=0,padx=5, pady=5)
btn2.grid(row=4,column=1,padx=5, pady=5)
btn3.grid(row=4,column=2,padx=5, pady=5)
btn_resta.grid(row=4,column=3,padx=5, pady=5)

btn0.grid(row=5,column=0, columnspan = 2, padx=5, pady=5)
btndot.grid(row=5,column=2,padx=5, pady=5)
btnequal.grid(row=5,column=3,padx=5, pady=5)



root.mainloop()