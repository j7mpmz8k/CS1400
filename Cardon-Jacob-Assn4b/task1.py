# Jacob Cardon
# CS1400 - MWF - 8:30am

#### Add Import Statement(s) as needed ####
from chessboard import draw_chessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    start_x = int(input("Welcome to Chessmate"
                      "\n\tEnter a starting x position: "))
    start_y = int(input("\tEnter a starting y position: "))
    width = input("\tEnter a width: ")
    height = input("\tEnter a height: ")
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        draw_chessboard(start_x, start_y)
    elif height == "":
        draw_chessboard(start_x, start_y, width=int(width))
    elif width == "":
        draw_chessboard(start_x, start_y, height=int(height))
    else:
        draw_chessboard(start_x, start_y, int(width), int(height))

main()