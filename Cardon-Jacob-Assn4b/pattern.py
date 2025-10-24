# Jacob Cardon
# CS1400 - MWF - 8:30am
import math
import drawly
import random
from random import randint


def setup():
    drawly.start("Patterns", background="white")
    drawly.set_speed(10)

def reset():
    drawly.set_color("white")
    drawly.rectangle(0, 0, 720, 1280)
    drawly.draw()

def draw_rectangle_pattern(center_x:int, center_y:int, offset:int, width:int, height:int,  count:int, rotaton:int) -> None:
    for angle in [i * 360.0 / count for i in range(count)]:  # incriments list of fractional angles with 'count' number of angles
        x_from_0, y_from_0 = get_distance_point(offset, angle)
        rectangle_x_start = center_x + x_from_0
        rectangle_y_start = center_y + y_from_0
        set_random_color()
        drawly.rectangle(rectangle_x_start, rectangle_y_start, width, height, stroke=2,
                         rotation_degrees=round(angle * -1 + rotaton * -1), rotation_point=(rectangle_x_start, rectangle_y_start))
        drawly.draw()

def draw_circle_pattern(center_x:int, center_y:int, offset:int, radius:int, count:int) -> None:
    for angle in [i * 360.0 / count for i in range(count)]:#incriments list of fractional angles with 'count' number of angles
        x_from_0, y_from_0 = get_distance_point(offset + radius, angle)
        circle_center_x = center_x + x_from_0
        circle_center_y = center_y + y_from_0
        set_random_color()
        drawly.circle(circle_center_x, circle_center_y, radius, stroke=2)
        drawly.draw()

def draw_super_pattern(pattern_count:int=5) -> None:
    for i in range(pattern_count):
        random_function = randint(0,1)
        center_x = randint(0, 1280)
        center_y = randint(0, 720)
        offset = randint(0, 100)
        width = randint(10, 100)
        height = randint(10, 100)
        radius = randint(10, 100)
        count = randint(3, 50)
        rotation = randint(0, 360)
        if random_function == 1:
            draw_rectangle_pattern(center_x, center_y, offset, width, height,  count, rotation)
        else:
            draw_circle_pattern(center_x, center_y, offset, radius, count)

def set_random_color() -> None:
    drawly.set_color(random.choice(["red", "green", "blue", "orange", "purple"]))

def get_distance_point(distance, angle):
    """returns x, y coordinate relative to 0, 0 at a given angle and distance.
    Simply add x, y to the center location of target to find new x,y"""
    x_pos = distance * math.cos(math.radians(angle))
    y_pos = distance * math.sin(math.radians(angle))
    return x_pos, y_pos
