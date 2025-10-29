# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from random import randint


class Treasure:
    pass

def make_treasure(png):
    treasure = Treasure()
    width:int = pygame.image.load(png).get_width()
    height:int = pygame.image.load(png).get_height()
    x_radius:int = round(width / 2)
    y_radius:int = round(height / 2)
    treasure.radius = width / 2
    treasure.center_pos = (randint(0 + x_radius, 600 - x_radius),
                           randint(round(0 + y_radius), 600 - y_radius))
    treasure.draw_pos = (treasure.center_pos[0] - x_radius,
                         treasure.center_pos[1] - y_radius)
    treasure.speed = 5
    treasure.dir = (2, 5)
    return treasure