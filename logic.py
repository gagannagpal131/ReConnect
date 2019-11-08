import re

# class_names = set([])


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

# Adding classnames to dictionaries for Inheritance, Methods and Variables

dictClassVariables = dict.fromkeys(classList, None)
dictClassInheritances = dict.fromkeys(classList, None)
dictClassMethods = dict.fromkeys(classList, None)


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

# print(classInheritenceList)


# Logic to find where each class ends

tempIndex = []
lineNumbersOfClassEnding = []        # It is used to hold line numbers of "};", which means, where each class ends. It
                                     # will be (actual line - 1) because index of listOflLines starts from 0

for i in range(0, len(listOfLines)):
    tempIndex.append(listOfLines[i].find('};'))
    if tempIndex[i] != -1:
        lineNumbersOfClassEnding.append(i)

print(lineNumbersOfClassEnding)


# Variables logic starts

def varExtIntDouble(inputStr):      # This method extracts variables (type int and double) and their datatype from
                                    # the passed string and return as array
    inputStr = inputStr.strip()     #To remove empty space from beginning of string
    if re.match(r".*\(+.*\)", inputStr):
        return None

    array = []
    x = re.split("\s|;|,|=|[0-9]", inputStr)

    for i in range(len(x)):
        if x[i] != "":
            array.append(x[i])
    return array

def varExtString(inputStr):
    inputStr = inputStr.strip();
    tempStr = inputStr.replace('string', '').replace(';', '')
    tempStr = tempStr.split(",")

    array = ["string"]

    for i in range(len(tempStr)):
        array.append(tempStr[i].split("=")[0].strip())  # Split on = for each entry in list | Get left element of =
                                                        # | strip extra spaces |
    return array


def getVariables():     #This method is for finding all variables of a class and adding in dictionary
    j = 0
    temparr = []
    temparr2 = []
    for i in range(0, len(lineNumbersOfClassEnding)):
        while j <= lineNumbersOfClassEnding[i]:
            startingWord = re.findall("^double|^int|^string", listOfLines[j].strip())
            # print(startingWord)
            if startingWord == ["int"] or startingWord == ["double"]:
                temparr = varExtIntDouble(listOfLines[j])
                if temparr is not None:
                    temparr2.append(temparr)
                    dictClassVariables[classList[i]] = temparr2
            elif startingWord == ["string"]:
                temparr = varExtString(listOfLines[j])
                if temparr is not None:
                    temparr2.append(temparr)
                    dictClassVariables[classList[i]] = temparr2

            j = j+1
        temparr2 = []
    # print(temparr2)
    print(dictClassVariables)

getVariables()

