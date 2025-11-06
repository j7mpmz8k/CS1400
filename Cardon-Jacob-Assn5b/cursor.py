import pygame

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

class Cursor:
    def __init__(self, mode, image, screen, scale=.05):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
        self.screen = screen
        original_image = pygame.image.load(image)
        orig_width, orig_height = original_image.get_size()
        new_width = int(SCREEN_WIDTH * scale)# Calculate target width (e.g., 5% of screen width)
        new_height = int(orig_height * (new_width / orig_width))# Calculate target height based on aspect ratio
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.pos = [0, 0]# draw position
        self.offset = [-self.rect.width / 2, -self.rect.height / 2]

        # Add collision bounding box attribute
        if mode == "catching":
            collision_width = self.rect.width * .37
            collision_height = self.rect.height * 0.34
            collision_x_pos = self.rect.width * .62 + collision_width + self.rect.left
            collision_y_pos= self.rect.height * .06 + collision_height + self.rect.top
            self.collision_rect = pygame.Rect(collision_x_pos, collision_y_pos, collision_width, collision_height)
        elif mode == "killing":
            collision_height = self.rect.height * 0.2
            collision_y_pos = self.rect.height * .03 + collision_height + self.rect.top
            self.collision_rect = pygame.Rect(self.rect.left, collision_y_pos, self.rect.width, collision_height)

    def update_pos(self, mouse_pos):
        """calculates draw position of cursor based on mouse position"""
        self.pos = [
                mouse_pos[0] + self.offset[0],
                mouse_pos[1] + self.offset[1]
                ]

        self.pos[0] = 0 if self.pos[0] < 0 else self.pos[0]
        self.pos[0] = SCREEN_WIDTH - self.rect.width if self.pos[0] > SCREEN_WIDTH - self.rect.width else self.pos[0]
        self.pos[1] = 0 if self.pos[1] < 0 else self.pos[1]
        self.pos[1] = SCREEN_HEIGHT - self.rect.height if self.pos[1] > SCREEN_HEIGHT - self.rect.height else self.pos[1]

    def draw(self):
        self.screen.blit(self.image, self.pos)
