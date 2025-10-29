# Jacob Cardon
# CS1400 - MWF - 8:30am
import pygame
from math import dist
from player import Player, make_player, move_player
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

    boing = pygame.mixer.Sound("task1_assets/boing.mp3")

    pygame.mixer.music.load("task1_assets/music.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    ##########
    # Set up game data
    ##########
    bomb_move = [10, 5]#direction and speed
    person_move = 5  # just speed
    person = make_player("task1_assets/pig.png")
    bomb = make_enemy("task1_assets/pig.png")
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
                move_player(person, [0, -person_move])
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                move_player(person, [0, person_move])
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                move_player(person, [-person_move, 0])
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                move_player(person, [person_move, 0])

        ##########
        # Update state of components/data
        ##########
        #### Always Update ####

        game_over = True if dist(bomb.center_pos, person.center_pos) <= bomb.radius + person.radius else not True

        #### Update if Game is Not Over ####
        if not game_over:
            bomb_move[0] *= -1 if bomb.is_off_screen(bomb_move)[0] else 1
            bomb_move[1] *= -1 if bomb.is_off_screen(bomb_move)[1] else 1
            move_enemy(bomb, bomb_move)
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
        screen.blit(person.picture, person.draw_pos)
        screen.blit(bomb.picture, bomb.draw_pos)
        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()
