# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from random import randint


class Player:
    pass

def make_player(self, png):
    player = Player()
    width: int = pygame.image.load(png).get_width()
    height: int = pygame.image.load(png).get_height()
    x_radius: int = round(width / 2)
    y_radius: int = round(height / 2)
    player.radius = width / 2
    player.center_pos = (randint(0 + x_radius, 600 - x_radius),
                         randint(round(0 + y_radius), 600 - y_radius))
    player.draw_pos = (player.center_pos[0] - x_radius,
                       player.center_pos[1] - y_radius)
    player.speed = 5
    player.dir = (2, 5)
    return player