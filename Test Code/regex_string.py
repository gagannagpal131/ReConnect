#This is to implement string searching in the program
import re

inputStr = "String temp = \"C++ and Python\", temp2=\"Java\", temp3 = \"xyz\""

# Check if "String" is present at the beginning of a word:

datatype = re.findall("^String", inputStr)

array = [datatype[0]]

print("Datatype =", array[0])

##### When declaration is like "String temp="Hello!", temp2 = "Bye!" "
tempStr = inputStr.replace('String', '')
tempStr = tempStr.split(",")

for i in range(len(tempStr)):
    array.append(tempStr[i].split("=")[0].strip())    ###Split on = for each entry in list | Get left element of = | strip extra spaces |

print("Variables =")
for i in range(1, len(array)):
    print(array[i])

print(array)
