
import re
str = "int a=100,b=9,c;"

# Check if "int" is present at the beginning of a word:

datatype = re.findall("^int", str)

array = [datatype[0]]

print("Datatype =", array[0])

##### When declaration is like "int a=10,b=10,d,d;"
#There can be space between the strings.
x = re.split("\s|;|,|=|[0-9]", str)
x.remove("int")

for i in x:
    x.remove("")

for i in range(len(x)):
    if x[i] != "":
        array.append(x[i])
"""
print("Variables =")
for i in range(1, len(array)):
    print(array[i])
"""
print(array)
