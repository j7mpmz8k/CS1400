# Jacob Cardon
# CS1400 - MWF - 8:30am
import drawly

# window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_dimension = 1920
y_dimension = 1080


def x_ratio(x_ratio):
    """Converts a position by percentage of screen aspect ratio to pixel coordinate (0 = left, 100 = right)"""
    return int(x_dimension * x_ratio / 100)


def y_ratio(y_ratio):
    """Converts a position by percentage of screen aspect ratio to pixel coordinate (0 = bottom, 100 = top)"""
    return int(y_dimension * (100 - y_ratio) / 100)


def x_reverse_ratio(x_pixels):
    """Converts pixel coordinate to screen aspect ratio"""
    return x_pixels * 100 / x_dimension


def y_reverse_ratio(y_pixels):
    """Converts pixel coordinate to screen aspect ratio"""
    return -1 * ((((100 * y_pixels) / y_dimension)) - 100)


class Shape:
    sides:int
    color:str
    size:str
    def draw(self, x, y):

shapes = []