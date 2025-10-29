# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from player import Player, make_player
from enemy import Enemy, make_enemy
from treasure import Treasure, make_treasure

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600
CLOCK_TICK = 30
TITLE = "Window Name"

def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    boing = pygame.mixer.Sound("task1_assets/boing.mp3")

    pygame.mixer.music.load("task1_assets/music.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    ##########
    # Set up game data
    ##########

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
