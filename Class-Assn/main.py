import drawly
#window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 1920
y_pixels = 1080

#converts a position by percentage to pixel coordinate
def x_ratio(x_ratio):
    return x_pixels * x_ratio / 100
def y_ratio(y_ratio):
    return y_pixels*(100-y_ratio)/100

# Window + background
drawly.start("Grid", dimensions=(x_pixels, y_pixels), background="skyblue", terminal=True, terminal_lines=6)
drawly.set_speed(5)  # slow enough to see each element appear

#horizontal grid lines
y_grid_incriments = 5
y_pos_start = 0
y_grid_text = True
for i in range(int(100/y_grid_incriments)):
    drawly.set_color("magenta")
    drawly.line(0, y_ratio(y_pos_start), x_pixels, y_ratio(y_pos_start))
    drawly.set_color("darkgreen")
    if y_grid_incriments >= 3:#prints all text when larger grid incriments
        drawly.text(0, y_ratio(y_pos_start), f'{int(y_pos_start)}%')
    elif y_grid_text == True:#skips every other text label to avoid text overlap in small incriments
        drawly.text(0, y_ratio(y_pos_start), f'{int(y_pos_start)}%')
    y_grid_text = not y_grid_text
    y_pos_start += y_grid_incriments

#vertical grid lines
x_grid_incriments = 5
x_pos_start = 0
x_grid_text = True
for i in range(int(100/x_grid_incriments)):
    drawly.set_color("magenta")
    drawly.line(x_ratio(x_pos_start), 0, x_ratio(x_pos_start), y_pixels)
    drawly.set_color("darkgreen")
    if x_grid_incriments >= 3:#prints all text when larger grid incriments
        drawly.text(x_ratio(x_pos_start + .2), y_ratio(3), f'{int(x_pos_start)}%')
    elif x_grid_text == True:#skips every other text label to avoid text overlap in small incriments
        drawly.text(x_ratio(x_pos_start + .2), y_ratio(3), f'{int(x_pos_start)}%')
    x_grid_text = not x_grid_text
    x_pos_start += x_grid_incriments
drawly.draw()


# number1 = drawly.terminal_input("enter a number")
# drawly.terminal_output(number1)

# Draw the mouth arc, adjusting for the bounding rectangle of the arc function.
drawly.set_color(blue)
drawly.arc(x_ratio(50) - x_ratio(50), y_ratio(50) - mouth_radius, 2 * mouth_radius, 2 * mouth_radius,
           mouth_start_angle, mouth_end_angle, mouth_thickness)
drawly.draw()


drawly.draw()
drawly.done()