import math
import os

file = os.path.expanduser('massInputForPart2')

with open(file, 'r') as massFile:
    values = massFile.read()
    print("Reading values from txt file---")
    print(values)

#  we have to splits mass values
splittedValues = values.splitlines()
print("splitted value--")
print(splittedValues)
print()