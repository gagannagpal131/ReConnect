#This file is to implement the UI for the logic.
from tkinter import *

window = Tk()
my_var = " hello"
window.title("Welcome to ReConnect: Class Level Architecture Recovery")

lbl = Label(window, text="Hello"+my_var)

lbl.grid(column=300, row=300)

window.mainloop()
