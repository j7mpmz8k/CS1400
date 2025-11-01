# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from random import randint

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600

class Treasure:
    pass

def make_treasure(picture_file:str) -> object:
    """makes treasure object and returns it. Sets up treasure's initial position, radius, and draw position."""
    treasure = Treasure()
    treasure.picture = pygame.image.load(picture_file)
    width:int = treasure.picture.get_width()
    height:int = treasure.picture.get_height()
    x_radius:float = width / 2
    y_radius:float = height / 2
    treasure.radius = min(x_radius, y_radius)
    treasure.center_pos = [randint(round(0 + x_radius), round(SCREEN_WIDTH - x_radius)), #randomly positioned on screen
                           randint(round(0 + y_radius), round(SCREEN_HEIGHT - y_radius))]
    treasure.draw_pos = [treasure.center_pos[0] - x_radius,#caluclated from center position
                         treasure.center_pos[1] - y_radius]
    treasure.is_collected = False
    return treasure