# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from random import randint


class Enemy:
    pass

def make_enemy(self, png):
    enemy = Enemy()
    width: int = pygame.image.load(png).get_width()
    height: int = pygame.image.load(png).get_height()
    x_radius: int = round(width / 2)
    y_radius: int = round(height / 2)
    enemy.radius = width / 2
    enemy.center_pos = (randint(0 + x_radius, 600 - x_radius),
                        randint(round(0 + y_radius), 600 - y_radius))
    enemy.draw_pos = (enemy.center_pos[0] - x_radius,
                      enemy.center_pos[1] - y_radius)
    enemy.speed = 5
    enemy.dir = (2, 5)
    return enemy