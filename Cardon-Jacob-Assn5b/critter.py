# Jacob Cardon
# CS1400 - MWF - 8:30am

from random import randint
import pygame

screen_width = 0
screen_height = 0

class Critter:
    def __init__(self, screen:object, type:str, image:str, scale:float=0.05):
        global screen_width, screen_height
        screen_width, screen_height = screen.get_size()
        self.screen = screen
        original_image = pygame.image.load(image)
        orig_width, orig_height = original_image.get_size()
        new_width = int(SCREEN_WIDTH * scale)  # Calculate target width (e.g., 5% of screen width)
        new_height = int(orig_height * (new_width / orig_width))  # Calculate target height based on aspect ratio
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        self.rect = self.picture.get_rect(center=(screen_width / 2, screen_height / 2))  # Directly set center position
        self.radius = min(self.rect.width / 2, self.rect.height / 2)  # Compute radius as half the smaller dimension
        self.move = [randint(-15, 15), randint(-15, 15)]
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
        The parameter is the [x, y] location of the mouse (or what you consider to be the main point of your tool)
        Returns the critter type if it was hit
        Returns another value if it was not hit
        """
        pass