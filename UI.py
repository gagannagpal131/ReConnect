#This file is to implement the UI for the logic.
import logic
import tkinter as tk
from random import randint

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
    heading = tk.Label(windowNew,text="Class: "+className,pady=20,bg='SteelBlue1',font=("Helvetica", 20,"bold"))
    heading.pack()
    #windowStart = 500+(counter*300)
    windowStart = 500+randint(100,700)
    windowNew.geometry('550x700+%d+%d'%(windowStart,0))
    windowNew['bg'] = 'SteelBlue1'

    #Adding inheritences
    Section1 = tk.Text(windowNew, height=10, width=55)
    Section1['bg'] = 'LightBlue1'
    Section1['font'] = "helvetica 14 bold"
    Section1.pack(pady = 20)
    Section1.insert(tk.END, 'Classes Inherited by class '+className+ ' are given below:\n\n')
    if className in dictClassInheritances:
        Section1.insert(tk.END, 'Format: <Access Specifier>  <Class Name>\n\n')
        st1=dictClassInheritances[className]
        for i in st1:
            Section1.insert(tk.END, i+'\n')
    else:
        Section1.insert(tk.END, 'No Classes are Inherited by this class\n')
    #w = tk.Label(Section1, text=dictClassInheritances[st1])
    #w.pack()

    #Adding methods
    Section2 = tk.Text(windowNew, height=10, width=55)
    Section2['bg'] = 'LightBlue1'
    Section2['font'] = "helvetica 14 bold"
    Section2.pack(pady = 20)
    Section2.insert(tk.END, 'Methods present in class '+className+ ' are given below:\n\n')
    if className in dictClassMethods:
        Section2.insert(tk.END, 'Format: <Return Type>  <Method Name>\n\n')
        st2=dictClassMethods[className]
        for i in st2:
            Section2.insert(tk.END, i+'\n')
    else:
        Section2.insert(tk.END, 'No methods are defined in this class\n')

    #Adding variabless
    Section3 = tk.Text(windowNew, height=10, width=55)
    Section3['bg'] = 'LightBlue1'
    Section3['font'] = "helvetica 14 bold"
    Section3.pack(pady = 20)
    Section3.insert(tk.END, 'Variables present in class '+className+ ' are given below:\n\n')
    if className in dictClassVariables:
        Section3.insert(tk.END, 'Format: <Type>  <Variable Name>\n\n')
        st3=dictClassVariables[className]
        for i in st3:
            Section3.insert(tk.END, i+'\n')
    else:
        Section2.insert(tk.END, 'No variables are defined in this class\n')


window = tk.Tk()
window.title("ReConnect: Class Level Architecture Recovery")
window.geometry('600x1000')
window['bg'] = 'SteelBlue1'

heading = tk.Label(window,text="ReConnect: Class Level Architecture Recovery",pady=25,bg='SteelBlue1',font=("Helvetica", 25,"bold"))
heading.pack()

heading1 = tk.Label(window,text="All the classes present in the Input source are \ngiven below:",pady=15,bg='SteelBlue1',font=("Helvetica", 20))
heading1.pack()

heading2 = tk.Label(window,text="Click on a class to view its \nInheritance, Methods and Variables!",pady=15,bg='SteelBlue1',font=("Helvetica", 20))
heading2.pack()


for i in range (0, len(classList)):
    button = tk.Button(window, width=30, text=classList[i],command=lambda i = i: printClassDetails(classList[i]))
    button.pack(side=tk.TOP,pady=18)

window.mainloop()
