# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from math import dist

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600

class Player:
    def update_draw_pos(self) -> None:
        """never called directly, called by move_player() and .reset()"""
        self.draw_pos = [self.center_pos[0] - self.x_radius,
                         self.center_pos[1] - self.y_radius]
    def reset(self) -> None:
        """resets center and drawing position to initialization"""
        self.center_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT - self.y_radius]
        self.update_draw_pos()

def make_player(picture_file:str) -> object:
    """initializes player object and returns it. Sets up player's initial position, radius, and draw position."""
    player = Player()
    player.picture = pygame.image.load(picture_file)
    width:int = player.picture.get_width()
    height:int = player.picture.get_height()
    player.x_radius = width / 2
    player.y_radius = height / 2
    player.radius = min(player.x_radius, player.y_radius)
    player.center_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT - player.y_radius]#centered at bottom of screen
    player.draw_pos = [player.center_pos[0] - player.x_radius,#caluclated from center position
                       player.center_pos[1] - player.y_radius]
    return player

def move_player(player: object, direction: list) -> None:
    """
    Updates center x,y postions and drawing start position. Displayed on screen at end of game loop
    """
    new_x = player.center_pos[0] + direction[0]
    new_y = player.center_pos[1] + direction[1]
    # updates x & y position if player is within the screen
    if player.radius <= new_x <= SCREEN_WIDTH - player.radius and player.radius <= new_y <= SCREEN_HEIGHT - player.radius:
        player.center_pos[0] = new_x
        player.center_pos[1] = new_y
        player.update_draw_pos()

def did_touch(player:object, item:object) -> bool:
    """returns True if player and specified item are within radius distance of each other"""
    return dist(player.center_pos, item.center_pos) <= player.radius + item.radius