# Jacob Cardon
# CS1400 - MWF - 8:30am
import drawly
from random import randrange
from math import cos, sin, radians
#window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 2560
y_pixels = 1440

def x_ratio(x_ratio):
    """Converts a position by percentage to pixel coordinate (0 = left, 100 = right)"""
    return x_pixels * x_ratio / 100
def y_ratio(y_ratio):
    """Converts a position by percentage to pixel coordinate (0 = bottom, 100 = top)"""
    return y_pixels * (100 - y_ratio) / 100

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

target_x = x_ratio(int(input("Enter the X location for the target: ")))
target_y = y_ratio(int(input("Enter the Y location for the target: ")))
target_location = target_x, target_y
target_size = x_ratio(int(input("Enter the size of the target: ")))

dart_size = x_ratio(5)
dart_offset_distance = (target_size / 2) + (dart_size / 2)
num_of_darts = int(input("How many darts would you like? "))

drawly.start(title="dart board", background="white", dimensions=(x_pixels, y_pixels-150), terminal=True, terminal_lines=3, terminal_line_height=50)
drawly.set_speed(9)

draw_circle(target_location, target_size, fill="blue")
draw_circle(target_location, target_size*.66, fill="yellow")
draw_circle(target_location, target_size*.33, fill="red")

for dart_num in range(1,num_of_darts+1):
    drawly.terminal_input(f"Press enter to throw dart #{dart_num}: ")
    dart_rotation = randrange(360)
    dart_offset_location = (target_x + dart_offset_distance * cos(radians(dart_rotation)),
                            target_y + dart_offset_distance * sin(radians(dart_rotation)))
    draw_circle(dart_offset_location, dart_size, fill="purple")
drawly.terminal_output("Try again next time!")

drawly.done()