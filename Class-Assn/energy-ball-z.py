# energy-ball-z.py

import pygame


SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720
CLOCK_TICK = 15  # TODO: try different frame rates
TITLE = "Energy Ball Z"


class EnergyBall:
    """Maintains the position and image of an energy ball"""
    def __init__(self, image, position):
        self.image = image
        self.radius = image.get_width() / 2
        self.position = position
    
    def draw(self, surface):
        """Draw the energy ball centered on its position"""
        draw_pos = [self.position[0] - self.radius,
                    self.position[1] - self.radius]
        surface.blit(self.image, draw_pos)

    def clicked(self, mouse_pos):
        """Return True|False based on whether the mouse position is within this energy ball's radius"""
        dx = mouse_pos[0] - self.position[0]
        dy = mouse_pos[1] - self.position[1]
        dist = (dx ** 2 + dy ** 2) ** 0.5
        return dist <= self.radius


def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    # Load all EnBall sprites in sequence
    sprites = [
            pygame.image.load("assets/EnBallBlue.png"),
            pygame.image.load("assets/EnBallRed.png"),
            pygame.image.load("assets/EnBallGreen.png"),
            pygame.image.load("assets/EnBallYellow.png"),
            pygame.image.load("assets/EnBallPurp.png"),
            ]
    
    pygame.mouse.set_visible(False)
    
    ##########
    # Set up game data
    ##########
    current_sprite_index = 0  # Index of current cursor sprite
    placed_energy_balls = []  # List of EnergyBall instances

    ##########
    # Game Loop
    ##########
    game_over = False
    running = True
    while running:
        ##########
        # Get Input/Events
        ##########
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicked the window's X button
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    ### Do Stuff to Reset Game ###
                    # TODO: Remove all EnergyBalls and clear the canvas
                    print("Canvas is cleared")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # TODO: Create and place an EnergyBall at click position
                    print("EnergyBall placed at", event.pos)
                    # TODO: Advance to next sprite (cycle through all sprites)
                    current_sprite_index = current_sprite_index + 1 if current_sprite_index < len(sprites) - 1 else 0
                    print("Now using sprite #" + str(current_sprite_index))
                elif event.button == 3:  # Right mouse button
                    # TODO: Remove the energy balls that were right-clicked
                    removed_count = 0
                    print("Removed", removed_count, "EnergyBalls")


        ##########
        # Update state of components/data
        ##########
        #### Always Update ####
        mouse_pos = pygame.mouse.get_pos()

        #### Update if Game is Not Over ####
        if not game_over:
            pass
        #### Update if Game is Over ####
        else:
            pass

        ##########
        # Update Display
        ##########
        #### Always Display ####
        screen.fill("black")
        
        # Draw all placed energy balls
        for energy_ball in placed_energy_balls:
            energy_ball.draw(screen)
        
        # Draw current cursor sprite at mouse position
        current_sprite = sprites[current_sprite_index]
        cursor_rect = current_sprite.get_rect()
        cursor_rect.center = mouse_pos
        screen.blit(current_sprite, cursor_rect)

        #### Display while Game is being played ####
        if not game_over:
            pass
        #### Display while Game is Over ####
        else:
            pass

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
