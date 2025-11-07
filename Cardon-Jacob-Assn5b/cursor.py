# Jacob Cardon
# CS1400 - MWF - 8:30am

from pygame import *

screen_width = 0
screen_height = 0

class Cursor:
    screen: Surface
    image: Surface
    rect: Rect
    collision_radius: float
    offset: tuple[int, int]
    collision_center: tuple[int, int]
    sound: mixer.Sound

    def __init__(self, game_mode:str, sound, image_path:str, screen:Surface, scale=.05) -> None:
        global screen_width, screen_height
        screen_width, screen_height = screen.get_size()
        self.screen = screen
        original_image = image.load(image_path)
        orig_width, orig_height = original_image.get_size()
        new_width = int(screen_width * scale)  # Calculate target width (e.g., 5% of screen width)
        new_height = int(orig_height * (new_width / orig_width))  # Calculate target height based on aspect ratio
        self.image = transform.scale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.sound = sound

        # Add collision bounding box attribute
        if game_mode == "catching":
            self.collision_radius = self.rect.width * .38 / 2
            self.offset = (
                round(self.rect.width / 2 + self.collision_radius),
                round(self.rect.height * .05 + self.collision_radius)
            )
        elif game_mode == "killing":
            self.collision_radius = self.rect.width / 2  # Already rounded, but consistent
            self.offset = (
                round(self.rect.width / 2),
                round(self.rect.height * .015 + self.collision_radius)
            )

        self.collision_center = (0 + self.offset[0], 0 + self.offset[1])#initialized to top left corner of screen

    def update_pos(self, mouse_pos: tuple[int, int]) -> None:
        """Calculates draw position of cursor based on mouse position, ensuring collision center aligns with mouse when possible."""
        # Set collision position to mouse position initially
        self.collision_center = mouse_pos

        # Calculate top-left draw position based on collision offset
        self.rect.topleft = (
            int(self.collision_center[0] - self.offset[0]),
            int(self.collision_center[1] - self.offset[1])
        )
        # Clamp the rectangle to stay within screen bounds
        self.rect.topleft = (
            max(0, min(screen_width - self.rect.width, self.rect.left)),
            max(0, min(screen_height - self.rect.height, self.rect.top))
        )
        # Recalculate collision center based on clamped rect position
        self.collision_center = (
            self.rect.left + self.offset[0],
            self.rect.top + self.offset[1]
        )

    def draw(self) -> None:
        self.screen.blit(self.image, self.rect.topleft)