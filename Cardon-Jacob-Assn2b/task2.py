# Jacob Cardon
# CS1400 - MWF - 8:30am

import drawly
from math import inf

# window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 1920
y_pixels = 1080

def x_ratio(x_ratio):
    """Converts a position by percentage of screen aspect ratio to pixel coordinate (0 = left, 100 = right)"""
    return int(x_pixels * x_ratio / 100)
def y_ratio(y_ratio):
    """Converts a position by percentage of screen aspect ratio to pixel coordinate (0 = bottom, 100 = top)"""
    return int(y_pixels * (100 - y_ratio) / 100)
def draw_circle(center_location, width, outline_thickness=0, outline="black", fill="white"):
    """allows to draw either a filled cicle or an outline...\n
    center_location=(x,y)...width=diameter"""
    center_x_pos, center_y_pos = center_location
    if outline_thickness > 0:
        drawly.set_color(outline)
        drawly.circle(center_x_pos, center_y_pos, width / 2, outline_thickness)
    else:
        drawly.set_color(fill)
        drawly.circle(center_x_pos, center_y_pos, width / 2)
    drawly.draw()
def distance(point1, point2):
    """calculates the pixel count distance between two points...\n
    point=(x,y)"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
def calculate_overlap(point1, size1, point2, size2):
    """checks how many pixels two circles overlap...\n
    point=(x,y)...size=diameter"""
    radius1 = size1 / 2
    radius2 = size2 / 2
    return (radius1 + radius2) - distance(point1, point2)


print("\nWelcome to Superhero Decisions")
print("For size and coordinate values, please enter 0-100 representing percentage of screen size")
# hero build
hero_name = input("For the Superhero enter...\n...Name: ")
hero_size = x_ratio(int(input("...Size: ")))#diameter
hero_x_location = x_ratio(int(input("...X Location(0-100 left to right): ")))
hero_y_location = y_ratio(int(input("...Y Location(0-100 bottom to top): ")))
hero_location = hero_x_location, hero_y_location

#arms
hero_arm_length = x_ratio(int(input("...Arm length: ")))#radius
#attack stored as a diameter from arm length extended from edge of hero's body
super_punch = (hero_arm_length * 2) + hero_size

#legs
hero_leg_length = -inf
#makes sure input for leg length is greater than arm length
while hero_leg_length <= hero_arm_length:
    print(f"Leg length must be greater than arm length: {hero_arm_length}")
    hero_leg_length = x_ratio(int(input("...Leg length: ")))#radius
    if hero_leg_length <= hero_arm_length:
        print("Invalid input. Please try again.")
#attack stored as a diameter from leg length extended from edge of hero's body
ninja_kick = (hero_leg_length * 2) + hero_size

#sword
hero_sword_length = -inf
while hero_sword_length + hero_arm_length <= hero_leg_length:
    print("Sword + arm Length must be greater than leg length:")
    print(f"Sword length must be greater than: {hero_leg_length-hero_arm_length}")
    hero_sword_length = x_ratio(int(input("...Sword length: ")))#radius
    if hero_sword_length + hero_arm_length <= hero_leg_length:
        print("Invalid input. Please try again.")
#attack stored as a diameter from sum of arm and sword length extended from edge of hero's body
samurai_slash = (hero_sword_length * 2) + (hero_arm_length * 2) + hero_size

#voice power
hero_voice_length = -inf
#must be greater than arm+sword length emenating from center of body
while hero_voice_length < hero_arm_length + hero_sword_length:
    print(f"Voice Length must be greater than arm and sword length: {hero_arm_length + hero_sword_length}")
    hero_voice_length = x_ratio(int(input("...Voice length: ")))#radius
    if hero_voice_length < hero_arm_length + hero_sword_length:
        print("Invalid input. Please try again.")
#creates attack as diameter extended from center of hero's body
sonic_blast = hero_voice_length * 2

print(f"\nWelcome superhero {hero_name}, please keep us all safe!\n")

#villain build
villain_name = input("For the Villain enter...\n...Name: ")
overlap = inf
#gets user input for villains size and location...ensures villain's body doesn't overlap with hero
while overlap > 0:
    print("Please enter the following using values: 0-100 representing percentage of screen size")
    villain_size = x_ratio(int(input("...Body Size: ")))#diameter
    villain_x_location = x_ratio(int(input("...X Location(0-100 left to right): ")))
    villain_y_location = y_ratio(int(input("...Y Location(0-100 bottom to top): ")))
    villain_location = villain_x_location, villain_y_location
    overlap = calculate_overlap(hero_location, hero_size, villain_location, villain_size)
    if overlap > 0:
        print("\nInvalid input. Must not overlap with hero. Please try again.")

print(f"\nOh no! The evil villain {villain_name} has appeared!")
#instructions to user to fight villain
input(f"Hit Enter to help {hero_name} fight {villain_name}: ")


drawly.start(title=f"{hero_name} vs {villain_name}", dimensions=(x_pixels, y_pixels-50),
             terminal=True, terminal_lines=1, terminal_line_height=50)
drawly.set_speed(9)

#draws hero and villain as filled in circle
draw_circle(hero_location, width=hero_size, fill="tan")
draw_circle(villain_location, width=villain_size, fill="black")

#availbe attack actions...sizes stored as diameters
powers = {
    1:{"name":"super punch", "size":super_punch, "color":"blue"},
    2:{"name":"ninja kick", "size":ninja_kick, "color":"green"},
    3:{"name":"samurai slash", "size":samurai_slash, "color":"red"},
    4:{"name":"sonic blast", "size":sonic_blast, "color":"purple"}
}
#placeholder to find the best attack as a king of the hill method...must be least non negative overlap with villain
best_attack = {"name":None, "overlap":inf}
#loop for both drawing each attack circumference, and finding the best attack to use
for power in powers:#"power"=key names, not an index
    draw_circle(hero_location, powers[power]["size"], outline_thickness=3, outline=powers[power]["color"])
    overlap = calculate_overlap(hero_location, powers[power]["size"], villain_location, villain_size)
    #finds the least non negative overlap of the attack action with the villain
    if 0 < overlap < best_attack["overlap"]:
        best_attack["name"] = powers[power]["name"]
        best_attack["overlap"] = overlap
#checks if villain is out of range from hero's attacks
if best_attack["name"] == None:
    defeat_message = f"Oh no! {villain_name} is too far away!"
    print(defeat_message)
    drawly.terminal_output(defeat_message)
else:
    #if in range, displays best attack
    success_message = f"{hero_name}'s best attack is {best_attack['name']}!"
    print(success_message)
    drawly.terminal_output(success_message)

drawly.done()