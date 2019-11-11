#This file is to implement the UI for the logic.
import logic
import tkinter as tk

classList, dictClassInheritances,dictClassMethods,dictClassVariables = logic.returnToUI()

#print(classList)
#print()
#print(dictClassInheritances)
#print()
#print(dictClassMethods)
#print()
#print(dictClassVariables)
#print()

def printClassDetails(className):
    print (className)

window = tk.Tk()
window.title("ReConnect: Class Level Architecture Recovery")
window.geometry('700x1000')
window['bg'] = 'LightBlue1'

for i in range (0, len(classList)):
    button = tk.Button(window, width=30, text=classList[i],command=lambda className = classList[i]: printClassDetails(className))
    button.pack(side=tk.TOP,pady=20)

window.mainloop()
