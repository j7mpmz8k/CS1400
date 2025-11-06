# Jacob Cardon
# CS1400 - MWF - 8:30am

from random import randint
from pygame import *
from math import dist

screen_width = 0
screen_height = 0

class Critter:
    screen: Surface
    image: Surface
    rect: Rect
    radius: float
    move: tuple[int, int]
    type: str

    def __init__(self, type:str, image_path:str, screen:Surface, scale:float=0.05):
        global screen_width, screen_height
        screen_width, screen_height = screen.get_size()
        self.screen = screen
        original_image = image.load(image_path)
        orig_width, orig_height = original_image.get_size()
        new_width = int(screen_width * scale)  # Calculate target width (e.g., 5% of screen width)
        new_height = int(orig_height * (new_width / orig_width))  # Calculate target height based on aspect ratio
        self.image = transform.scale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))  # Directly set center position
        self.radius = min(self.rect.width / 2, self.rect.height / 2)  # Compute radius as half the smaller dimension
        self.move = (randint(-15, 15), randint(-15, 15))
        self.type = type

    def draw(self):
        """Draw the image on the screen in the appropriate spot"""
        self.screen.blit(self.image, self.rect.topleft)

    def move_critter(self):
        """
        Again, you can name this something different if your theme is different.
        Update the position of the critter
        """
        self.rect = self.rect.move(self.move[0], self.move[1])
        self.check_bounce()

    def check_bounce(self):
        """
        This might be a little different than other ways we've bounced things off walls
        The critter will detect if it hit a wall or not and will adjust its move list appropriately
        Hint: You can get the dimensions of the screen from the screen parameter in the initializer: get_width() and get_height() will do it.
        Note: The entire image should always be on the screen. When the edge of the image hits a side, it should bounce.
        """

        hit_left = self.rect.left <= 0
        hit_right = self.rect.right >= screen_width
        hit_top = self.rect.top <= 0
        hit_bottom = self.rect.bottom >= screen_height
        if hit_left:
            self.rect.left = 0
            self.move[0] *= -1
        if hit_right:
            self.rect.right = screen_width
            self.move[0] *= -1
        if hit_top:
            self.rect.top = 0
            self.move[1] *= -1
        if hit_bottom:
            self.rect.bottom = screen_height
            self.move[1] *= -1

    def did_get(self, cursor):
        """
        Returns the critter type if it was hit
        Returns another value if it was not hit
        """
        return self.type if dist(self.rect.center, cursor.collision_center) <= self.radius + cursor.collision_radius else False