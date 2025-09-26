# Jacob Cardon
# CS1400 - MWF - 8:30am
import drawly, random
from random import randint, randrange
from random import randrange
#window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 1920
y_pixels = 1080

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
    center_x_pos = x_ratio(center_x_pos)
    center_y_pos = y_ratio(center_y_pos)
    if outline_thickness > 0:
        drawly.set_color(outline)
        drawly.circle(center_x_pos, center_y_pos, x_ratio(width) / 2, outline_thickness)
    else:
        drawly.set_color(fill)
        drawly.circle(center_x_pos, center_y_pos, x_ratio(width) / 2)
    drawly.draw()
def distance(point1, point2):
    """calculates the pixel count distance between two points...\n
    point=(x,y)"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x_ratio(x2) - x_ratio(x1))**2 + (y_ratio(y2) - y_ratio(y1))**2)**0.5
def calculate_overlap(point1, size1, point2, size2):
    """checks how many pixels two circles overlap...\n
    point=(x,y)...size=diameter"""
    radius1 = size1 / 2
    radius2 = size2 / 2
    return (x_ratio(radius1) + x_ratio(radius2)) - distance(point1, point2)

target_x = int(input("Enter the X location for the target"))
target_y = int(input("Enter the Y location for the target"))
location =(target_x, target_y)
target_size = int(input("Enter the size of the target"))

draw_circle(location, target_size, fill="blue")
draw_circle(location, target_size*.66, fill="yellow")
draw_circle(location, target_size*.33, fill="red")

dart_location = randrange(100), randrange(100)
dart_size = 5
dart_rotation = randrange(360)
dart_offset_distance = (target_size / 2) + (dart_size / 2)
dart_offset_location =
draw_circle(dart_location, dart_size, fill="purple")