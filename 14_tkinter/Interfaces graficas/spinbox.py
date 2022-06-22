from tkinter import *

root = Tk()
root.geometry("400x300")

w = Spinbox(root, values= ('Python','Html5', 'Java', 'Js'))
w.pack()


root.mainloop()