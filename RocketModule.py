import math
import os

file = os.path.expanduser('massInput.txt')

# totalFuelRequirement = 0

with open(file, 'r') as massFile:
    values = massFile.read()
    print("Reading values from txt file---")
    print(values)

#  we have to splits mass values
splittedValues = values.splitlines()
print("splitted value--")
print(splittedValues)
print()
