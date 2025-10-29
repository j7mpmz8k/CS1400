# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from random import randint

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600

class Treasure:
    pass

def make_treasure(png):
    treasure = Treasure()
    width:int = pygame.image.load(png).get_width()
    height:int = pygame.image.load(png).get_height()
    treasure.picture = pygame.image.load(png)
    treasure.radius = round(min(width, height) / 2)
    treasure.center_pos = [randint(0 + treasure.radius, SCREEN_WIDTH - treasure.radius),
                           randint(0 + treasure.radius, SCREEN_HEIGHT - treasure.radius)]
    treasure.draw_pos = [treasure.center_pos[0] - treasure.radius,
                         treasure.center_pos[1] - treasure.radius]
    return treasure