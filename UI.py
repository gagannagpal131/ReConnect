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
    #Creating new window
    windowNew = tk.Tk()
    windowNew.title(className)
    windowNew.geometry('500x350')
    windowNew['bg'] = 'LightBlue1'

    #Adding inheritences 
    st1=dictClassInheritances[className]
    Section1 = tk.Text(windowNew, height=6, width=30)
    Section1.pack()    
    #w = tk.Label(Section1, text=dictClassInheritances[st1])
    #w.pack()
    for i in st1:
       Section1.insert(tk.END, i+'\n')

    #Adding methods
    st2=dictClassMethods[className]
    Section2 = tk.Text(windowNew, height=6, width=30)
    Section2.pack()
    for i in st2:
        Section2.insert(tk.END, i+'\n')
       
    #Adding variables
    st3=dictClassVariables[className]
    Section3 = tk.Text(windowNew, height=6, width=30)
    Section3.pack()
    for i in st3:
        Section3.insert(tk.END, i+'\n')
       

window = tk.Tk()
window.title("ReConnect: Class Level Architecture Recovery")
window.geometry('700x1000')
window['bg'] = 'LightBlue1'

for i in range (0, len(classList)):
    button = tk.Button(window, width=30, text=classList[i],command=lambda i = i: printClassDetails(classList[i]))
    button.pack(side=tk.TOP,pady=20)

window.mainloop()
