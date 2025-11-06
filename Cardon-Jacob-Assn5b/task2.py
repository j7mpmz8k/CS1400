# Jacob Cardon
# CS1400 - MWF - 8:30am

from critter import *
from cursor import *
import pygame
from time import time

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

    critter_images = ["assets2/butterfly.png", "assets2/wasp.png"]
    critter_count = 10
    critter_list = make_critter_list(10, screen, critter_images)

    background = pygame.image.load("assets2/background.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ##########
    # Set up game data
    ##########

    cursor = net
    time_start = round(time(), 2)

    ##########
    # Game Loop
    ##########
    game_over = False
    running = True
    game_won = None
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    temp_list = []
                    for critter in critter_list:
                        if critter.did_get(cursor) == "good" and cursor == spray:
                            game_over = True
                            losing_msg = "You killed a butterfly!"
                        elif critter.did_get(cursor) == "bad" and cursor == net:
                            game_over = True
                            losing_msg = "You caught a wasp!"
                        elif critter.did_get(cursor) == "good" and cursor == net:
                            cursor = spray
                        elif critter.did_get(cursor) == "bad" and cursor == spray:
                            cursor = net
                        elif not critter.did_get(cursor):
                            temp_list.append(critter)
                    critter_list = temp_list


        ##########
        # Update state of components/data
        ##########
        #### Always Update ####


        #### Update if Game is Not Over ####
        if not game_over:
            if critter_list == []:
                game_won = True
                game_over = True
                time_end = round(time(), 2)
                time_elapsed = time_end - time_start
            else:
                for critter in critter_list:
                    critter.move_critter()
                    cursor.update_pos(pygame.mouse.get_pos())
        #### Update if Game is Over ####
        else:
            if game_won:
                # winning message
                game_over_msg = font.render(f"You did it in {time_elapsed} seconds", True, text_color)
                game_over_msg_pos = game_over_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # draw pos to center on screen
            else:
                # losing message
                game_over_msg = font.render(losing_msg, True, text_color)
                game_over_msg_pos = game_over_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  # draw pos to center on screen

        ##########
        # Update Display
        ##########
        #### Always Display ####
        screen.blit(background, (0, 0))

        #### Display while Game is being played ####
        if not game_over:
            cursor.draw()
            for critter in critter_list:
                critter.draw()
        #### Display while Game is Over ####
        else:
            screen.blit(game_over_msg, game_over_msg_pos)

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)

main()
