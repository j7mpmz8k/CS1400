# Jacob Cardon
# CS1400 - MWF - 8:30am

import pygame


def main():
    # Standard Pygame Setup. Include for every pygame program
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # Starting State of objects
    x_pos = 640
    y_pos = 360
    radius = 25

    x_dir = 14
    y_dir = 8

    # Create a sound effect
    boing = pygame.mixer.Sound("boing.mp3")

    # Create background music and start it
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    running = True

    while running:
        # Get Input/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # User clicked the window's X button
                running = False

        # Update the Game State
        if x_pos + radius >= 1280 or x_pos - radius <= 0:
            x_dir = x_dir * -1
            pygame.mixer.Sound.play(boing)

        if y_pos + radius >= 720 or y_pos - radius <= 0:
            y_dir = y_dir * -1
            pygame.mixer.Sound.play(boing)

        x_pos += x_dir
        y_pos += y_dir

        # Update/Redraw the display
        screen.fill("white")  # Filling the screen wipes out any previous screen content
        pygame.draw.circle(screen, "black", [x_pos, y_pos], radius)
        pygame.display.flip()

        clock.tick(30)  # Max Frames Per Second is 30

    pygame.quit()

main()