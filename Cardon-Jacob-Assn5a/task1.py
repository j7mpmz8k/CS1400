# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from player import Player, make_player, move_player, did_touch
from enemy import Enemy, make_enemy, move_enemy
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

    collected = pygame.mixer.Sound("task1_assets/collected.wav")
    boing = pygame.mixer.Sound("task1_assets/boing.mp3")

    pygame.mixer.music.load("task1_assets/Kim Lightyear - Starlight.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    ##########
    # Set up game data
    ##########
    ninja_move = [10, 5]#direction and speed
    alien_move = 5  # just speed
    ninja = make_enemy("task1_assets/ninja.png")
    alien = make_player("task1_assets/spaceship.png")
    treasure_list = [make_treasure("task1_assets/pig.png") for i in range(10)]

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
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                move_player(alien, [0, -alien_move])
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                move_player(alien, [0, alien_move])
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                move_player(alien, [-alien_move, 0])
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                move_player(alien, [alien_move, 0])

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####


        #### Update if Game is Not Over ####
        if not game_over:
            game_over = True if did_touch(alien, ninja) else not True
            if ninja.is_off_screen(ninja_move)[0]:
                ninja_move[0] *= -1
                pygame.mixer.Sound.play(boing)
            if ninja.is_off_screen(ninja_move)[1]:
                ninja_move[1] *= -1
                pygame.mixer.Sound.play(boing)
            move_enemy(ninja, ninja_move)
            for i in treasure_list:
                if did_touch(alien, i) and not i.is_collected:
                    pygame.mixer.Sound.play(collected)
                    i.is_collected = True

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
        screen.fill("white")  # Filling the screen wipes out any previous screen content
        screen.blit(alien.picture, alien.draw_pos)
        screen.blit(ninja.picture, ninja.draw_pos)
        for treasure in treasure_list:
            screen.blit(treasure.picture, treasure.draw_pos) if not treasure.is_collected else None
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
