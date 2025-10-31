# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600

class Enemy:
    def update_draw_pos(self) -> None:
        """never called directly, called by move_enemy() and .reset()"""
        self.draw_pos:list = [self.center_pos[0] - self.x_radius,
                         self.center_pos[1] - self.y_radius]
    def is_on_screen(self, direction:list) -> list[bool]:
        """returns two bool values representing if new x,y position is still on the screen."""
        in_x_axis = self.x_radius <= self.center_pos[0] + direction[0] <= SCREEN_WIDTH - self.x_radius
        in_y_axis = self.y_radius <= self.center_pos[1] + direction[1] <= SCREEN_HEIGHT - self.y_radius
        return [in_x_axis, in_y_axis]
    def reset(self) -> None:
        """resets center and drawing position to initialization"""
        self.center_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
        self.update_draw_pos()

def make_enemy(picture_file:str) -> object:
    """initializes enemy object and returns it. Sets up enemy's initial position, radius, and draw position."""
    enemy = Enemy()
    enemy.picture = pygame.image.load(picture_file)
    width:int = enemy.picture.get_width()
    height:int = enemy.picture.get_height()
    enemy.x_radius = width / 2
    enemy.y_radius = height / 2
    enemy.radius = min(enemy.x_radius, enemy.y_radius)
    enemy.center_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]#centered in the middle of screen
    enemy.draw_pos = [enemy.center_pos[0] - enemy.x_radius,#caluclated from center position
                      enemy.center_pos[1] - enemy.y_radius]
    return enemy

def move_enemy(enemy:object, direction:list) -> None:
    """Updates center x,y postions and drawing start position. Displayed on screen at end of game loop"""
    enemy.center_pos[0] += direction[0]
    enemy.center_pos[1] += direction[1]
    enemy.update_draw_pos()