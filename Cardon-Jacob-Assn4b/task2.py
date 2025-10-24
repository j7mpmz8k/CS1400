# Jacob Cardon
# CS1400 - MWF - 8:30am
import pattern
from pattern import draw_super_pattern


def main():
    # Setup target
    pattern.setup()

    # Play again loop
    play_again = True

    print("Welcome to Patterns!!!")
    print()

    while play_again:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("\t1) Rectangle")
        print("\t2) Circle")
        print("\t3) Super Pattern")
        mode = int(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle'
        if mode == 1:
            print("You chose Rectangle Pattern")
            #### Add Input Statement(s) as needed ####
            center_x = int(input("Enter a center x position: "))
            center_y = int(input("Enter a center y position: "))
            offset = int(input("Enter an offset: "))
            height = int(input("Enter a height: "))
            width = int(input("Enter a width: "))
            count = int(input("Enter a count: "))
            rotation = int(input("Enter a rotation: "))
            #### End Add Inputs Statement(s) ####

            # Draw a single rectangle pattern
            pattern.draw_rectangle_pattern(center_x, center_y, offset, height, width, count, rotation)

        # If they choose Circle
        elif mode == 2:
            print("You chose Circle Pattern")
            #### Add Input Statement(s) as needed ####
            center_x = int(input("Enter a center x position: "))
            center_y = int(input("Enter a center y position: "))
            offset = int(input("Enter an offset: "))
            radius = int(input("Enter a radius: "))
            count = int(input("Enter a count: "))
            #### End Add Inputs Statement(s) ####

            # Draw a single circle pattern
            pattern.draw_circle_pattern(center_x, center_y, offset, radius, count)

        # If they choose super mode
        elif mode == 3:
            print("You chose Super Pattern")
            #### Add Input Statement(s) as needed ####
            num = int(input("Number? "))
            draw_super_pattern(num)
            #### End Add Inputs Statement(s) ####

            # Draw super pattern
            if num == "":
                pattern.draw_super_pattern()
            else:
                pattern.draw_super_pattern(int(num))

        # Play again?
        print("Do you want to play again?")
        print("\t1) Yes, and keep drawings")
        print("\t2) Yes, and clear drawings")
        print("\t3) No, I am all done")
        response = int(input("Choose 1, 2, or 3: "))
        print()

        #### Add Statement(s) to clear drawings and play again ####
        if response == 2:
            pattern.reset()
        if response == 3:
            play_again = False
        #### End Add Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")


main()
