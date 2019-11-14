import re

with open('SampleCPP.cpp') as file:
    listOfLines = file.readlines()

# Classname logic
def getClassNames():
    classListTmp1 = []  # Array of All the lines which start with the word 'class'
    for i in range(0, len(listOfLines)):
        listOfLines[i] = listOfLines[i].replace('\n', '')
        listOfLines[i] = listOfLines[i].replace('{', '')
        if re.match("^class", listOfLines[i]):
            classListTmp1.append(listOfLines[i])
    # print(classListTmp1)

    global classList
    classList = []  # Array of All the Class Names

    for i in range(0, len(classListTmp1)):
        classList.append(classListTmp1[i].split(" ")[1])
    #print(classList)

    # Adding classnames to dictionaries for Inheritance, Methods and Variables
    global dictClassVariables, dictClassInheritances, dictClassMethods
    dictClassVariables = dict.fromkeys(classList, None)
    dictClassInheritances = dict.fromkeys(classList, None)
    dictClassMethods = dict.fromkeys(classList, None)


# Inheritance logic
def getInheritanceList():
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

    #print(classInheritenceList)
    #print(dictClassInheritances)

    for i in range (0,len(classInheritenceList)):
        dictClassInheritances[classInheritenceList[i][0]] = []
    #print(dictClassInheritances)


    for i in range(0,len(classInheritenceList)):
        #print(classInheritenceList[i][0])
        for j in range(1, len(classInheritenceList[i])):
            dictClassInheritances[classInheritenceList[i][0]].append(classInheritenceList[i][j])
            #print(classInheritenceList[i][j])

    #print(dictClassInheritances)


# Logic to find where each class ends
def getClassEndings():
    tempIndex = []
    global lineNumbersOfClassEnding
    lineNumbersOfClassEnding = []        # It is used to hold line numbers of "};", which means, where each class ends.
                                         # It will be (actual line - 1) because index of listOflLines starts from 0

    for i in range(0, len(listOfLines)):
        tempIndex.append(listOfLines[i].find('};'))
        if tempIndex[i] != -1:
            lineNumbersOfClassEnding.append(i)

    #print(lineNumbersOfClassEnding)

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

def varExtString(inputStr):         # This method extracts variables (type string) and their datatype from
                                    # the passed string and return as array
    inputStr = inputStr.strip();
    if re.match(r".*\(+.*\)", inputStr):
        return None

    tempStr = inputStr.replace('string', '').replace(';', '')
    tempStr = tempStr.split(",")

    array = ["string"]

    for i in range(len(tempStr)):
        array.append(tempStr[i].split("=")[0].strip())  # Split on = for each entry in list | Get left element of =
                                                        # | strip extra spaces |
    return array

def varExtChar(inputStr):       # This method extracts variables (type char) and their datatype from
                                    # the passed string and return as array
    inputStr = inputStr.strip();
    if re.match(r".*\(+.*\)", inputStr):
        return None

    tempStr = inputStr.replace('char', '').replace(';', '')
    tempStr = tempStr.split(",")

    array = ["char"]

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
            startingWord = re.findall("^double|^int|^string|^char", listOfLines[j].strip())
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
            elif startingWord == ["char"]:
                temparr = varExtChar(listOfLines[j])
                if temparr is not None:
                    temparr2.append(temparr)
                    dictClassVariables[classList[i]] = temparr2
            j = j+1
        temparr2 = []
    # print(temparr2)
    #print(dictClassVariables)


def getFunctions():     #This method is for finding all Functions of a class and adding in dictionary
    j = 0
    temparr = []
    for i in range(0, len(lineNumbersOfClassEnding)):
        while j <= lineNumbersOfClassEnding[i]:
            startingWord = re.findall("^int|^string|^void", listOfLines[j].strip())
            if re.match(r".*\(+.*\)", listOfLines[j]):
                x = re.split("\s|\(", listOfLines[j].strip())
                temparr.append(x[0])
                temparr.append(x[1])
                dictClassMethods[classList[i]] = temparr
            j = j + 1
        temparr = []
    #print(dictClassMethods)


def createFinalStorage():

    getClassNames()
    getInheritanceList()
    getClassEndings()
    getVariables()
    getFunctions()

    #code to remove key:None values from the dictionaries
    toDeleteNone = []
    for key in dictClassInheritances:
        #print(key)
        if dictClassInheritances[key] == None:
            toDeleteNone.append(key)

    for i in toDeleteNone:
        del dictClassInheritances[i]
        #print()

    toDeleteNone = []
    for key in dictClassMethods:
        #print(key)
        if dictClassMethods[key] == None:
            toDeleteNone.append(key)

    for i in toDeleteNone:
        del dictClassMethods[i]
        #print()
    #print(dictClassMethods)

    toDeleteNone = []
    for key in dictClassVariables:
        #print(key)
        if dictClassVariables[key] == None:
            toDeleteNone.append(key)

    for i in toDeleteNone:
        del dictClassVariables[i]
        #print()
    #print(dictClassVariables)

    #Code to setup the "dictClassMethods"
    print()

    tempDict = dictClassMethods.copy()
    for key in tempDict:
        dictClassMethods[key] = []
        i = 0;
        while((i+1) <= len(tempDict[key])):
            my_str = tempDict[key][i]+" " + tempDict[key][i+1]
            i = i + 2
            #print(my_str)
            (dictClassMethods[key]).append(my_str)
    #print(dictClassMethods)

    #Code to setup the "dictClassVariables"
    tempDict = dictClassVariables.copy()
    for key in tempDict:
        #print(tempDict[key])
        dictClassVariables[key] = []
        for j in tempDict[key]:
            #print(len(j))
            #print(j)
            for k in range(1,len(j)):
                my_str = j[0] +" "+j[k];
                (dictClassVariables[key]).append(my_str)


#This function is to be called in UI.py to get the dictionaries with data.
def returnToUI():

    createFinalStorage()
    return classList, dictClassInheritances,dictClassMethods,dictClassVariables
