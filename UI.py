#This file is to implement the UI for the logic.
import logic
from tkinter import *

classList, dictClassInheritances,dictClassMethods,dictClassVariables = logic.returnToUI()
print(classList)
print()
print(dictClassInheritances)
print()
print(dictClassMethods)
print()
print(dictClassVariables)
print()

"""
window = Tk()
my_var = " hello"
window.title("Welcome to ReConnect: Class Level Architecture Recovery")

lbl = Label(window, text="Hello"+my_var)

lbl.grid(column=300, row=300)

window.mainloop()
"""
