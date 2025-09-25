# Jacob Cardon
# CS1400 - MWF - 8:30am
import drawly, random
from random import randint, randrange

window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 1920
y_pixels = 1080


def x_ratio(x_ratio):
    """Converts a position by percentage to pixel coordinate (0 = left, 100 = right)"""
    return x_pixels * x_ratio / 100

def y_ratio(y_ratio):
    """Converts a position by percentage to pixel coordinate (0 = bottom, 100 = top)"""
    return y_pixels * (100 - y_ratio) / 100

def size_ratio(size_ratio):
    """used for naming purposes; functionally the same as x_ratio()"""
    return x_pixels * size_ratio / 100

def draw_circle(center_x_pos, center_y_pos, width, fill="white", outline_thickness=0, outline="black"):
    """automatically adds an outline without having to add it as another function seperate from the fill"""
    drawly.set_color(fill)
    drawly.circle(center_x_pos, center_y_pos, width / 2)
    if outline_thickness > 0:
        drawly.set_color(outline)
        drawly.circle(center_x_pos, center_y_pos, width / 2, outline_thickness)
    drawly.draw()

# streamlines native Drawly arguments of starting and ending angle, combined into just "rotation" (ie. 90=normal, increasing value=counterclockwise rotation)
def draw_arc(color, center_x_pos, center_y_pos, width, hight, rotation=90, thickness=1):
    """Start angle ads 90 to get 180 and end angle adds 270 to get 360.
    This is needed to achieve a horizontally leveled arc. This draw_arc defines this as 90 degrees."""
    radius = width / 2
    drawly.set_color(color)
    drawly.arc(center_x_pos - radius, center_y_pos - radius, width, hight, start=90 + rotation, end=270 + rotation,
               stroke=thickness)
    drawly.draw()

# horizontal grid lines
y_grid_incriments = 5
y_pos_start = 0
y_grid_text = True
for i in range(int(100 / y_grid_incriments)):
    drawly.set_color("magenta")
    drawly.line(0, y_ratio(y_pos_start), x_pixels, y_ratio(y_pos_start))
    drawly.set_color("darkgreen")
    if y_grid_incriments >= 3:  # prints all text when larger grid incriments
        drawly.text(0, y_ratio(y_pos_start), f'{int(y_pos_start)}%')
    elif y_grid_text == True:  # skips every other text label to avoid text overlap in small incriments
        drawly.text(0, y_ratio(y_pos_start), f'{int(y_pos_start)}%')
    y_grid_text = not y_grid_text
    y_pos_start += y_grid_incriments

# vertical grid lines
x_grid_incriments = 5
x_pos_start = 0
x_grid_text = True
for i in range(int(100 / x_grid_incriments)):
    drawly.set_color("magenta")
    drawly.line(x_ratio(x_pos_start), 0, x_ratio(x_pos_start), y_pixels)
    drawly.set_color("darkgreen")
    if x_grid_incriments >= 3:  # prints all text when larger grid incriments
        drawly.text(x_ratio(x_pos_start + .2), y_ratio(3), f'{int(x_pos_start)}%')
    elif x_grid_text == True:  # skips every other text label to avoid text overlap in small incriments
        drawly.text(x_ratio(x_pos_start + .2), y_ratio(3), f'{int(x_pos_start)}%')
    x_grid_text = not x_grid_text
    x_pos_start += x_grid_incriments
drawly.draw()

color_code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def random_color():
    for i in range(len(color_code)):

#draw_circle(randrange(x_pixels), randrange(y_pixels),1, )
