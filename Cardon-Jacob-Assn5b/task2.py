# Jacob Cardon
# CS1400 - MWF - 8:30am

from critter import *
from cursor import *
import pygame

SCREEN_WIDTH = 1280  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 720
CLOCK_TICK = 30
TITLE = "Critter Catcher"

def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    ##########
    # Set up game media images, sounds
    ##########

    net = Cursor(game_mode="catching", image_path="assets2/net.png", screen=screen, scale=.1)
    spray = Cursor(game_mode="killing", image_path="assets2/spray.png", screen=screen, scale=.05)

    butterfly = Critter("good", "assets2/butterfly.png", screen, .05)

    background = pygame.image.load("assets2/background.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ##########
    # Set up game data
    ##########

    cursor = net

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
                if event.key == pygame.K_SPACE and game_over:
                    ### Do Stuff to Reset Game ###
                    game_over = False
            if event.type == pygame.MOUSEMOTION:
                cursor.update_pos(pygame.mouse.get_pos())

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####

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
        screen.blit(background, (0, 0))

        #### Display while Game is being played ####
        if not game_over:
            cursor.draw()
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
