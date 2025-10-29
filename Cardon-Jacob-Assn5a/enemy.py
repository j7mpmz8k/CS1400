# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600

class Enemy:
    def update_draw_pos(self) -> None:
        self.draw_pos:list = [self.center_pos[0] - self.radius,
                         self.center_pos[1] - self.radius]
    def is_off_screen(self, direction:list) -> list[bool, bool]:
        """returns two bool values representing if new x,y position is off screen"""
        at_x_axis = not(self.radius <= self.center_pos[0] + direction[0] <= SCREEN_WIDTH - self.radius)
        at_y_axis = not(self.radius <= self.center_pos[1] + direction[1] <= SCREEN_HEIGHT - self.radius)
        return [at_x_axis, at_y_axis]

def make_enemy(png):
    enemy = Enemy()
    width: int = pygame.image.load(png).get_width()
    height: int = pygame.image.load(png).get_height()
    enemy.picture = pygame.image.load(png)
    enemy.radius = min(width, height) / 2
    enemy.center_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
    enemy.draw_pos = [enemy.center_pos[0] - enemy.radius,
                      enemy.center_pos[1] - enemy.radius]
    return enemy

def move_enemy(enemy:object, direction:list) -> None:
    enemy.center_pos[0] += direction[0]
    enemy.center_pos[1] += direction[1]
    enemy.update_draw_pos()