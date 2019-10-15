import re

class_names = set([])

class_inheritance = {}
class_methods = {}
class_variables = {}









with open('SampleCPP.cpp') as file:
    listOfLines = file.readlines()



# Classname logic

# def name_of_classes():
classListTmp1 = []  # Array of All the lines which start with the word 'class'
for i in range(0, len(listOfLines)):
    listOfLines[i] = listOfLines[i].replace('\n', '')
    listOfLines[i] = listOfLines[i].replace('{', '')
    if "class" in listOfLines[i]:
        classListTmp1.append(listOfLines[i])
# print(classListTmp1)

classList = []  # Array of All the Class Names
for i in range(0, len(classListTmp1)):
    classList.append(classListTmp1[i].split(" ")[1])
# print(classList)



# Inheritance logic

classInheritenceListTmp1 = []
for i in range(0, len(listOfLines)):
    if re.match("^class.*protected", listOfLines[i]) or re.match("^class.*private", listOfLines[i]) or \
            re.match("^class.*public", listOfLines[i]):
        classInheritenceListTmp1.append(listOfLines[i])

# print(classInheritenceListTmp1)

classInheritenceListTmp2 = []
for i in range(0, len(classInheritenceListTmp1)):
    classInheritenceListTmp2.append(re.split(":|,", classInheritenceListTmp1[i]))

# print(classInheritenceListTmp2)

classInheritenceList = []  # Array of All the Class Inheritances by a class
for i in range(0, len(classInheritenceListTmp2)):
    # for j in range(0, len(classInheritenceListTmp2[i])-1):
    classInheritenceListTmp2[i][0] = classInheritenceListTmp2[i][0].replace("class", '')
    classInheritenceListTmp2[i][0] = classInheritenceListTmp2[i][0].strip()
    # classInheritenceListTmp2[i][j] = classInheritenceListTmp2[i][j].strip()
    classInheritenceList.append(classInheritenceListTmp2[i])

print(classInheritenceList)
# name_of_classes()
