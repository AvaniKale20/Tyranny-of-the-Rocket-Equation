import math
import os

file = os.path.expanduser('massInputForPart2')

with open(file, 'r') as massFile:
    values = massFile.read()
    print("Reading values from txt file---")
    print(values)