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
        # self.pos = [0, 0]# draw position
        self.rect = self.image.get_rect()
        # self.offset = [-self.rect.width / 2, -self.rect.height / 2]


        # Add collision bounding box attribute
        if mode == "catching":
            collision_width = self.rect.width * .37
            collision_height = self.rect.height * 0.34
            self.collision_offset = [self.rect.width * .62 + collision_width + self.rect.left,
                                     self.rect.height * .06 + collision_height + self.rect.top]
        elif mode == "killing":
            collision_width = self.rect.width
            collision_height = self.rect.height * 0.2
            self.collision_offset = [0, self.rect.height * .03 + collision_height + self.rect.top]

        self.collision_rect = pygame.Rect(self.rect.left + self.collision_offset[0],
                                          self.rect.top + self.collision_offset[1],
                                          collision_width, collision_height)

    def update_pos(self, mouse_pos):
        """calculates draw position of cursor based on mouse position"""
        # self.pos = [
        #         mouse_pos[0] + self.offset[0],
        #         mouse_pos[1] + self.offset[1]
        #         ]
        self.rect.center = mouse_pos

        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y))

        self.collision_rect.x = self.rect.x + self.collision_offset[0]
        self.collision_rect.y = self.rect.y + self.collision_offset[1]

    def draw(self):
        self.screen.blit(self.image, self.rect.topleft)
