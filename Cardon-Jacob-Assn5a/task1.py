# Jacob Cardon
# CS1400 - MWF - 8:30am

from player import *
from enemy import *
from treasure import *

SCREEN_WIDTH = 600  # Use constants here to be able to use in different places
SCREEN_HEIGHT = 600
CLOCK_TICK = 30
TITLE = "Collector Game"

def main():
    # Setup the pygame window and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ##########
    # Set up game media images, sounds
    ##########
    background = pygame.image.load("task1_assets/earth.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    collected_sound = pygame.mixer.Sound("task1_assets/collected.wav")
    collected_sound.set_volume(1.3)
    boing = pygame.mixer.Sound("task1_assets/boing.mp3")
    boing.set_volume(.3)
    defeat_sound = pygame.mixer.Sound("task1_assets/losetrumpet.mp3")
    victory_sound = pygame.mixer.Sound("task1_assets/Win sound.wav")


    pygame.mixer.music.load("task1_assets/Kim Lightyear - Starlight.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    font = pygame.font.SysFont("Comic Sans MS", 48, True)  # Font name and size
    text_color = (0, 0, 0)  # black

    losing_msg = font.render("Game Over! You lose!", True, text_color)  # Antialias enabled
    losing_msg_pos = losing_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    winning_msg = font.render("Game Over! You win!", True, text_color)  # Antialias enabled
    winning_msg_pos = winning_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))




    ##########
    # Set up game data
    ##########
    ninja_move = [12,-8]#direction and speed
    alien_move = 5  # just speed
    ninja = make_enemy("task1_assets/ninja.png")
    alien = make_player("task1_assets/spaceship.png")
    treasure_list = [make_treasure("task1_assets/pig.png") for i in range(10)]
    collected_list = []

    ##########
    # Game Loop
    ##########
    game_over = False
    running = True
    game_lost = None
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
                    for treasure in treasure_list:
                        treasure.reset()
                    collected_list = []
                    ninja.reset()
                    alien.reset()
                    pygame.mixer.music.play(-1)
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
            if did_touch(alien, ninja):
                game_over = True
                game_lost = True
                pygame.mixer.Sound.play(defeat_sound)
            if not ninja.is_on_screen(ninja_move)[0]:
                ninja_move[0] *= -1
                pygame.mixer.Sound.play(boing)
            if not ninja.is_on_screen(ninja_move)[1]:
                ninja_move[1] *= -1
                pygame.mixer.Sound.play(boing)
            move_enemy(ninja, ninja_move)
            for treasure in treasure_list:
                if did_touch(alien, treasure) and not treasure.is_collected:
                    pygame.mixer.Sound.play(collected_sound)
                    treasure.is_collected = True
                    collected_list.append(treasure)
            if len(collected_list) == len(treasure_list):
                game_over = True
                game_won = True
                pygame.mixer.Sound.play(victory_sound)

        #### Update if Game is Over ####
        else:
            pygame.mixer.music.stop()

        ##########a
        # Update Display
        ##########
        #### Always Display ####
        screen.fill("white")# Filling the screen wipes out any previous screen content
        screen.blit(background, (0, 0))

        #### Display while Game is being played ####
        if not game_over:
            screen.blit(alien.picture, alien.draw_pos)
            screen.blit(ninja.picture, ninja.draw_pos)
            for treasure in treasure_list:
                screen.blit(treasure.picture, treasure.draw_pos) if not treasure.is_collected else None
        #### Display while Game is Over ####
        else:
            screen.blit(losing_msg, losing_msg_pos) if game_lost else screen.blit(winning_msg, winning_msg_pos)


        #### Draw changes the screen ####

        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()