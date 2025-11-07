# Jacob Cardon
# CS1400 - MWF - 8:30am

from critter import *
from cursor import *
import pygame
from time import time

SCREEN_WIDTH = 1280
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



    critter_images = ["assets2/butterfly.png", "assets2/wasp.png"]

    background = pygame.image.load("assets2/background.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    font = pygame.font.SysFont("Comic Sans MS", 48, True)  # Font name and size

    pygame.mixer.music.load("assets2/music.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    successful_get_sound = pygame.mixer.Sound("assets2/successful_get.wav")
    successful_get_sound.set_volume(.5)
    swoosh_sound = pygame.mixer.Sound("assets2/swoosh.mp3")
    spray_sound = pygame.mixer.Sound("assets2/spray.mp3")
    spray_sound.set_volume(3)
    lose_sound = pygame.mixer.Sound("assets2/lose.mp3")
    win_sound = pygame.mixer.Sound("assets2/win.wav")

    net = Cursor(game_mode="catching", sound=swoosh_sound, image_path="assets2/net.png", screen=screen, scale=.1)
    spray = Cursor(game_mode="killing", sound=spray_sound, image_path="assets2/spray.png", screen=screen, scale=.05)



    ##########
    # Set up game data
    ##########

    cursor = net
    time_start = round(time(), 2)
    critter_count = 10
    critter_list = make_critter_list(critter_count, screen, critter_images)

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
            #exits window
            if event.type == pygame.QUIT:  # User clicked the window's X button
                running = False
            #quits game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                #restarts game
                if event.key == pygame.K_SPACE and game_over:
                    # increases count by 10 if win, sets back to 10 if loss
                    critter_count = 10 if not game_won else critter_count + 10
                    game_over = False
                    game_won = None
                    pygame.mixer.music.play(-1)
                    critter_list = make_critter_list(critter_count, screen, critter_images)
                    time_start = round(time(), 2)
            #moves mouse
            if event.type == pygame.MOUSEMOTION:
                cursor.update_pos(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound.play(cursor.sound)
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
                                pygame.mixer.Sound.play(lose_sound)
                        else:
                            caught_any = True
                    critter_list = temp_list

                    if not any(critter.type == "good" for critter in critter_list):
                        cursor = spray
                    elif not any(critter.type == "bad" for critter in critter_list):
                        cursor = net
                    else:
                        cursor = spray if cursor == net and caught_any else net
                    cursor.update_pos(pygame.mouse.get_pos())
                    pygame.mixer.Sound.play(successful_get_sound) if caught_any else None


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
                pygame.mixer.Sound.play(win_sound)
            else:
                for critter in critter_list:
                    critter.move_critter()

        #### Update if Game is Over ####
        if game_over:
            pygame.mixer.music.stop()
            text_color = (0, 255, 0)  if game_won else (255, 0, 0)
            play_again_msg = font.render(f"Press spacebar to play again!", True, text_color)
            play_again_msg_pos = play_again_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
            if game_won:
                # green winning message
                game_over_msg = font.render(f"You did it in {time_elapsed} seconds!", True, text_color)
                game_over_msg_pos = game_over_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            else:
                # red losing message
                game_over_msg = font.render(losing_msg, True, text_color)
                game_over_msg_pos = game_over_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

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
            screen.blit(play_again_msg, play_again_msg_pos)

        #### Draw changes the screen ####
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)

main()
