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
    critter_list = make_critter_list(critter_count, screen, critter_images)

    background = pygame.image.load("assets2/background.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.SysFont("Comic Sans MS", 48, True)  # Font name and size


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
                    critter_count += 10
                    game_over = False
                    game_won = None
                    critter_list = make_critter_list(critter_count, screen, critter_images)
            if event.type == pygame.MOUSEMOTION:
                cursor.update_pos(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    temp_list = []
                    caught_any = False
                    for critter in critter_list:
                        hit_result = critter.did_get(cursor)
                        if not hit_result:
                            temp_list.append(critter)
                        elif (hit_result == "good" and cursor == spray) or (hit_result == "bad" and cursor == net):
                                losing_msg = "You killed a butterfly!" if hit_result == "good" else "You caught a wasp!"
                                game_over = True
                                game_won = False
                        else:
                            caught_any = True
                    critter_list = temp_list
                    cursor = spray if cursor == net and caught_any else net
                    if len(critter_list) == 1:
                        cursor = spray if critter_list[0].type == "bad" else net


        ##########
        # Update state of components/data
        ##########
        #### Always Update ####


        #### Update if Game is Not Over ####
        if not game_over:
            if critter_list == []:
                game_won = True
                game_over = True
                time_end = time()
                time_elapsed = round(time_end - time_start, 2)
                # winning message
                text_color = (0, 255, 0)  # black
                game_over_msg = font.render(f"You did it in {time_elapsed} seconds!", True, text_color)
                game_over_msg_pos = game_over_msg.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))  # draw pos to center on screen
            else:
                for critter in critter_list:
                    critter.move_critter()
                    cursor.update_pos(pygame.mouse.get_pos())
        #### Update if Game is Over ####
        else:
            if game_won:
                pass
            else:
                # losing message
                text_color = (255, 0, 0)  # black
                game_over_msg = font.render(losing_msg, True, text_color)
                game_over_msg_pos = game_over_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))  # draw pos to center on screen

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
