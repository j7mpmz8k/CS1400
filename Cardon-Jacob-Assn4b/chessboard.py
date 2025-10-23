# Jacob Cardon
# CS1400 - MWF - 8:30am

import drawly

def draw_chessboard(start_x:int, start_y:int, width:int=250, height:int=250):
    drawly.start(title="chessmate", dimensions=(1280, 720), background="white")
    drawly.set_speed(10)
    draw_rectangle(start_x, start_y, width, height, border=True)
    draw_all_rectangles(start_x, start_y, width, height)
    drawly.done()

def draw_all_rectangles(start_x:int, start_y:int, width:int, height:int):
    width = width / 8
    height = height / 8
    black_tile = True
    for row in range(8):
        for col in range(8):
            draw_rectangle(start_x + col * width, start_y + row * height, width, height) if black_tile else None
            black_tile = not black_tile
        black_tile = not black_tile

def draw_rectangle(start_x:int, start_y:int, width:int|float, height:int|float, border:bool=False):
    drawly.set_color("black")
    drawly.polygon_begin(stroke=1) if border else drawly.polygon_begin()
    #sets up each of the 4 points for black tiles
    for point_modifier in [(0,0),(1,0),(1,1),(0,1)]:
        x, y = point_modifier
        drawly.add_poly_point(start_x + x * width, start_y + y * height)
    drawly.polygon_end()
    drawly.draw()