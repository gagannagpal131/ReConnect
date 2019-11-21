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
    #Creation of Class view
    windowNew = tk.Tk()
    windowNew.title(className)
    heading = tk.Label(windowNew,text="Class: "+className,pady=20,bg='grey1',fg='green1',font=("century gothic", 20,"bold"))
    windowNew['highlightcolor'] = 'blue'
    windowNew['highlightbackground'] = 'blue'
    windowNew['highlightthickness']=20
    heading.pack()
    #windowStart = 500+(counter*300)
    windowStart = 100+randint(100,700)
    windowNew.geometry('450x600+%d+%d'%(windowStart,0))
    windowNew['bg'] = 'grey1'

    #Adding inheritences
    Section1 = tk.Text(windowNew, height=7, width=45)
    Section1['bg'] = 'grey1'
    Section1['font'] = "calibri 13 bold"
    Section1['fg'] = 'green1'
    Section1['bd'] = 4
    Section1.pack(pady = 5)
    # Section1.insert(tk.END, 'Classes Inherited by class '+className+ ' are given below:\n\n')
    Section1.insert(tk.END, 'Classes Inherited:\n\n')
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
    Section2 = tk.Text(windowNew, height=7, width=45)
    Section2['bg'] = 'grey1'
    Section2['fg'] = 'green1'
    Section2['bd'] = 4
    Section2['font'] = "calibri 13 bold"
    Section2.pack(pady = 5)
    # Section2.insert(tk.END, 'Methods present in class '+className+ ' are given below:\n\n')
    Section2.insert(tk.END, 'Methods: \n\n')
    if className in dictClassMethods:
        Section2.insert(tk.END, 'Format: <Return Type>  <Method Name>\n\n')
        st2=dictClassMethods[className]
        for i in st2:
            Section2.insert(tk.END, i+'\n')
    else:
        Section2.insert(tk.END, 'No methods are defined in this class\n')

    #Adding variabless
    Section3 = tk.Text(windowNew, height=7, width=45)
    Section3['bg'] = 'grey1'
    Section3['fg'] = 'green1'
    Section3['bd'] = 4
    Section3['font'] = "calibri 13 bold"
    Section3.pack(pady = 5)
    # Section3.insert(tk.END, 'Variables present in class '+className+ ' are given below:\n\n')
    Section3.insert(tk.END, 'Variables: \n\n')
    if className in dictClassVariables:
        Section3.insert(tk.END, 'Format: <Type>  <Variable Name>\n\n')
        st3=dictClassVariables[className]
        for i in st3:
            Section3.insert(tk.END, i+'\n')
    else:
        Section3.insert(tk.END, 'No variables are defined in this class\n')

#Creation of Main View
window = tk.Tk()
window.title("ReConnect: Class Level Architecture Recovery")
window.geometry('600x700')
window['bg'] = 'Grey1'
window['highlightcolor'] = 'blue'
window['highlightbackground'] = 'blue'
window['highlightthickness']=30

heading = tk.Label(window,text="ReConnect\n Class Level Architecture Recovery ",pady=25,bg='grey1',fg='green1',relief='groove',bd=5,font=("century gothic", 25,"bold"))
heading.pack()

heading1 = tk.Label(window,text="All the classes present in the Input source are given below.\nClick on a class to view its Inheritance, Methods and Variables.",pady=20,bg='grey1',fg='green1',font=("calibri", 14))
heading1.pack()

for i in range (0, (int(len(classList)/2))):
    button = tk.Button(window, width=20, text=classList[i],fg='grey1',font=("calibri", 12,"bold"),command=lambda i = i: printClassDetails(classList[i])).place(x=50, y=200+(i*50))
    #button.pack(side=tk.TOP,pady=5)
    #button.grid(columnspan=3)

for i in range ((int(len(classList)/2)+1),len(classList)):
    button1 = tk.Button(window, width=20, text=classList[i],fg='grey1',font=("calibri", 12,"bold"),command=lambda i = i: printClassDetails(classList[i])).place(x=300, y=200+(i-(int(len(classList)/2))-1)*50)

window.mainloop()
