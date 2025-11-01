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
    #background image
    background = pygame.image.load("assets1/earth.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    #sound effects(collected, bounce, defeat, victory sounds)
    collected_sound = pygame.mixer.Sound("assets1/collected.wav")
    collected_sound.set_volume(1.3)
    boing = pygame.mixer.Sound("assets1/boing.mp3")
    boing.set_volume(.3)
    defeat_sound = pygame.mixer.Sound("assets1/losetrumpet.mp3")
    victory_sound = pygame.mixer.Sound("assets1/Win sound.wav")

    #background music
    pygame.mixer.music.load("assets1/Kim Lightyear - Starlight.mp3")
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1) # -1 loops the music continuously

    #text for game over messages(winning and loosing)
    font = pygame.font.SysFont("Comic Sans MS", 48, True)  # Font name and size
    text_color = (0, 0, 0)  # black
    #losing message
    losing_msg = font.render("Game Over! You lose", True, text_color)
    losing_msg_pos = losing_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))#draw pos to center on screen
    #winning message
    winning_msg = font.render("Game Over. You win!", True, text_color)
    winning_msg_pos = winning_msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))#draw pos to center on screen




    ##########
    # Set up game data
    ##########
    ninja_move = [12,-8]#direction and speed
    alien_move = 5  # just speed

    #makes all game objects with 10 treasures(pigs) to collect
    ninja = make_enemy("assets1/ninja.png")
    alien = make_player("assets1/spaceship.png")
    treasure_list = [make_treasure("assets1/pig.png") for i in range(10)]

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
            # User clicked the window's X button
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # quitting the game
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                # resetting the game
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
                    game_won = None
                    game_lost = None
                    #puts all treasures back on screen
                    treasure_list = [make_treasure("assets1/pig.png") for i in range(10)]
                    #resets to starting positions
                    ninja.reset()
                    alien.reset()

                    pygame.mixer.music.play(-1)

        if not game_over:
            #player movement controls
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
            move_enemy(ninja, ninja_move)
            #bouncing off the edges of the screen detection
            if not ninja.is_on_screen(ninja_move)[0]:
                ninja_move[0] *= -1
                pygame.mixer.Sound.play(boing)
            if not ninja.is_on_screen(ninja_move)[1]:
                ninja_move[1] *= -1
                pygame.mixer.Sound.play(boing)
            #collecting treasure detection
            temp_remaining_list = []
            for treasure in treasure_list:
                if did_touch(alien, treasure):
                    pygame.mixer.Sound.play(collected_sound)
                else:
                    temp_remaining_list.append(treasure)
            treasure_list = temp_remaining_list
            #winning condition check
            if treasure_list == []:
                game_over = True
                game_won = True
                pygame.mixer.Sound.play(victory_sound)
            #losing condition check
            elif did_touch(alien, ninja):
                game_over = True
                game_lost = True
                pygame.mixer.Sound.play(defeat_sound)

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
            #draws player, enenemy, and remaining treasures
            screen.blit(alien.picture, alien.draw_pos)
            screen.blit(ninja.picture, ninja.draw_pos)
            [screen.blit(treasure.picture, treasure.draw_pos) for treasure in treasure_list]
        #### Display while Game is Over ####
        else:
            #draws game over message
            screen.blit(losing_msg, losing_msg_pos) if game_lost else None
            screen.blit(winning_msg, winning_msg_pos) if game_won else None


        #### Draw changes the screen ####

        pygame.display.flip()

        ##########
        # Define the refresh rate of the screen
        ##########
        clock.tick(CLOCK_TICK)


main()