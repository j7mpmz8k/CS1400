# Jacob Cardon
# CS1400 - MWF - 8:30am

import drawly

def draw_chessboard(start_x:int, start_y:int, width:int=250, height:int=250):
    """Draws a chessboard with black and white tiles with a black border. Calls all other draw functions for board."""
    drawly.start(title="chessmate", background="white")
    drawly.set_speed(10)
    draw_rectangle(start_x, start_y, width, height, border=True)#boarder outline
    draw_all_rectangles(start_x, start_y, width, height)
    drawly.done()

def draw_all_rectangles(start_x:int, start_y:int, width:int, height:int):
    """draws all black tiles on the board"""
    width = width / 8
    height = height / 8
    black_tile = True#flips every other tile, then flips at start of row
    #sets up the 8x8 tiles and draws the black tiles
    for row in range(8):
        for col in range(8):
            draw_rectangle(start_x + col * width, start_y + row * height, width, height) if black_tile else None
            black_tile = not black_tile
        black_tile = not black_tile

def draw_rectangle(start_x:int, start_y:int, width:int|float, height:int|float, border:bool=False):
    """draws a single rectangle, with optional border instead of being filled"""
    drawly.set_color("black")
    drawly.polygon_begin(stroke=1) if border else drawly.polygon_begin()

    #sets up each of the 4 points for black tiles
    for point_modifier in [(0,0),(1,0),(1,1),(0,1)]:
        x, y = point_modifier
        drawly.add_poly_point(start_x + x * width, start_y + y * height)
    drawly.polygon_end()
    drawly.draw()