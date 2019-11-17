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
    #windowStart = 500+(counter*300)
    windowStart = 500;
    windowNew.geometry('400x600+%d+%d'%(windowStart,windowStart))
    windowNew['bg'] = 'LightBlue1'

    #Adding inheritences
    Section1 = tk.Text(windowNew, height=10, width=40)
    Section1.pack(pady = 20)
    if className in dictClassInheritances:
        Section1.insert(tk.END, 'Format: <Access Specifier> <Class Name>\n\n')
        st1=dictClassInheritances[className]
        for i in st1:
            Section1.insert(tk.END, i+'\n')
    else:
        Section1.insert(tk.END, 'No Classes are Inherited by this class\n')
    #w = tk.Label(Section1, text=dictClassInheritances[st1])
    #w.pack()

    #Adding methods
    Section2 = tk.Text(windowNew, height=10, width=40)
    Section2.pack(pady = 20)
    if className in dictClassMethods:
        Section2.insert(tk.END, 'Format: <Return Type> <Method Name>\n\n')
        st2=dictClassMethods[className]
        for i in st2:
            Section2.insert(tk.END, i+'\n')
    else:
        Section2.insert(tk.END, 'No methods are defined in this class\n')

    #Adding variables
    Section3 = tk.Text(windowNew, height=10, width=40)
    Section3.pack(pady = 20)
    if className in dictClassVariables:
        Section3.insert(tk.END, 'Format: <Type> <Variable Name>\n\n')
        st3=dictClassVariables[className]
        for i in st3:
            Section3.insert(tk.END, i+'\n')
    else:
        Section2.insert(tk.END, 'No variables are defined in this class\n')


window = tk.Tk()
window.title("ReConnect: Class Level Architecture Recovery")
window.geometry('500x1000')
window['bg'] = 'LightBlue1'

for i in range (0, len(classList)):
    button = tk.Button(window, width=30, text=classList[i],command=lambda i = i: printClassDetails(classList[i]))
    button.pack(side=tk.TOP,pady=20)

window.mainloop()
