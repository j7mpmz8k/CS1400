# Jacob Cardon
# CS1400 - MWF - 8:30am

from math import tan, pi
import math

def area_of_polygon(sides, length):
    """function assumes a regular polygon with equal lenghts per side"""
    return round((sides * math.pow(length,3)) / (4 * tan(pi / sides)), 5)

print("Welcome to the polygon calculator")

#stores user input
num_sides = []
lengths = []

#input accepts integers only for number of sides but does accept floats for side lengths
try:
    #poly one
    print("For polygon one, please enter...")
    num_sides.append(int(input("\tNumber of sides: ")))
    lengths.append(float(input("\tSide length: ")))
    #poly two
    print("For polygon two, please enter...")
    num_sides.append(int(input("\tNumber of sides: ")))
    lengths.append(float(input("\tSide length: ")))
    #poly three
    print("For polygon three, please enter...")
    num_sides.append(int(input("\tNumber of sides: ")))
    lengths.append(float(input("\tSide length: ")))
    #poly four
    print("For polygon four, please enter...")
    num_sides.append(int(input("\tNumber of sides: ")))
    lengths.append(float(input("\tSide length: ")))

except ValueError:
    print("\nERROR! Only whole numbers of sides per polygon are allowed.")

else:
    #loops through each polygon and prints both lists of sides and lengths
    for poly_index in range(4):
        poly_name = poly_index + 1
        print(f"The area of polygon {poly_name} is: {area_of_polygon(num_sides[poly_index], lengths[poly_index])}")