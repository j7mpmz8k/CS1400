# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600

class Player:
    def update_draw_pos(self) -> None:
        self.draw_pos = [self.center_pos[0] - self.radius,
                         self.center_pos[1] - self.radius]

def make_player(png):
    player = Player()
    width: int = pygame.image.load(png).get_width()
    height: int = pygame.image.load(png).get_height()
    player.picture = pygame.image.load(png)
    player.radius = min(width, height) / 2
    player.center_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT - player.radius]
    player.draw_pos = [player.center_pos[0] - player.radius,
                       player.center_pos[1] - player.radius]
    return player

def move_player(player: object, direction: list) -> None:
    new_x = player.center_pos[0] + direction[0]
    new_y = player.center_pos[1] + direction[1]
    # updates x & y position if player is within the screen
    if player.radius <= new_x <= SCREEN_WIDTH - player.radius and player.radius <= new_y <= SCREEN_HEIGHT - player.radius:
        player.center_pos[0] = new_x
        player.center_pos[1] = new_y
        player.update_draw_pos()