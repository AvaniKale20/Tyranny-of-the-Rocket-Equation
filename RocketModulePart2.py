import math
from math import floor
import os

file = os.path.expanduser('massInputForPart2')

with open(file, 'r') as massFile:
    values = massFile.read()
    print("Reading values from txt file---")
    print(values)

# we have to splits mass values
splittedValues = values.splitlines()
print("splitted value--")
print(splittedValues)
print()

calculated_fuel = 0
total_fuels=0


def calculateOfSubFuel(x):
    global calculated_fuel
    fuel_value = floor((int(x) / 3) - 2)

    if fuel_value < 0:
        return fuel_value
    print("fuel", fuel_value)
    calculated_fuel = calculated_fuel + fuel_value
    return calculateOfSubFuel(fuel_value)


print("calculation of sub fuel")
for n in splittedValues:
    calculateOfSubFuel(n)
print()
print("calculation of sub fuel --",calculated_fuel)


