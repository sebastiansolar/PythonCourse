from cmath import exp
import re
from tkinter import *

root = Tk()

root.title("Seba")

root.resizable(1,1)
root.iconbitmap("fire.ico")

miFrame = Frame(root)
#miFrame.pack(side="right", anchor="center")
miFrame.pack(fill="both", expand=1)
miFrame.config(width=400,height=350)
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")

root.config(cursor="boat")
root.config(bg="blue")
root.config(bd="25")
root.config(relief="sunken")

root.mainloop()