# Jacob Cardon
# CS1400 - MWF - 8:30am

import drawly

#window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 1920
y_pixels = 1080

#Converts a position by percentage to pixel coordinate (y inverted for top-left origin)
def x_ratio(x_ratio):
    return x_pixels * x_ratio / 100

def y_ratio(y_ratio):
    return y_pixels * (100 - y_ratio) / 100

#Converts a size by percentage to pixel value, using window width for scaling
def size_ratio(size_ratio):
    return x_pixels * size_ratio / 100

#Function to draw a filled circle with an optional outline for easier rendering of circular elements like the head and eyes.
def draw_circle(center_x_pos, center_y_pos, width, fill="white", outline_thickness=0, outline="black"):
    drawly.set_color(fill)
    drawly.circle(center_x_pos, center_y_pos, width/2)
    if outline_thickness > 0:
        drawly.set_color(outline)
        drawly.circle(center_x_pos, center_y_pos, width/2, outline_thickness)
    drawly.draw()

#streamlined native arc function arguments of starting and ending angle, combined into just "rotation" (ie. 90=normal, increasing value=counterclockwise rotation)
def draw_arc(color, center_x_pos, center_y_pos, width, hight, rotation=90, thickness=1):
    '''Start angle ads 90 to get 180 and end angle adds 270 to get 360.
    This is needed to achieve a horizontally leveled arc. This draw_arc defines this as 90 degrees.'''
    radius = width/2
    drawly.set_color(color)
    drawly.arc(center_x_pos - radius, center_y_pos - radius, width, hight, 90+rotation, 270+rotation, thickness)
    drawly.draw()

#Display a welcome message to the user in the IDE terminal, as it precedes window initialization.
print("Welcome to the Faceinator program. This application will guide you through creating a customized face drawing based on your inputs.")

#Prompt the user for their name using standard input, as required before initializing the Drawly window.
user_name = input("Please enter your name: ")

#Initialize the Drawly graphics window with a title incorporating the user's name, specified dimensions for scaling,
#and the terminal enabled for subsequent interactions.
drawly.start(title=f"{user_name}'s Faceinator", dimensions=(x_pixels, y_pixels), terminal=True)
drawly.terminal_clear()

#Output informational message to the Drawly terminal and gather input for the head.
drawly.terminal_output("NOTE! x/y Positions and size inputs are percentages of screen width/hight(0-100): x from left, y from bottom (0=bottom, 100=top).")
head_center_x = x_ratio(float(drawly.terminal_input("Enter the x-position for the center of the head (0-100): ")))
head_center_y = y_ratio(float(drawly.terminal_input("Enter the y-position for the center of the head (0-100): ")))
head_radius = size_ratio(float(drawly.terminal_input("Enter the width for the head (ie. 10 for 10% of width): ")))
head_color = drawly.terminal_input("Enter the color for the head: ")
draw_circle(head_center_x, head_center_y, head_radius, head_color, 2)

# dawing eyes based on user input using a custom circle function
drawly.terminal_output("NOTE! x/y Positions and size inputs are percentages of screen width/hight(0-100): x from left, y from bottom (0=bottom, 100=top).")
eye_color = drawly.terminal_input("Enter the color for both eyes: ")
#left eye
left_eye_x = x_ratio(float(drawly.terminal_input("Enter the x-position for the left eye (0-100): ")))
left_eye_y = y_ratio(float(drawly.terminal_input("Enter the y-position for the left eye (0-100): ")))
left_eye_size = size_ratio(float(drawly.terminal_input("Enter the size for the left eye (0-100): ")))
#right eye
right_eye_x = x_ratio(float(drawly.terminal_input("Enter the x-position for the right eye (0-100): ")))
right_eye_y = y_ratio(float(drawly.terminal_input("Enter the y-position for the right eye (0-100): ")))
right_eye_size = size_ratio(float(drawly.terminal_input("Enter the size for the right eye (0-100): ")))
#drawing both eyes
draw_circle(left_eye_x, left_eye_y, left_eye_size, eye_color, 1)
draw_circle(right_eye_x, right_eye_y, right_eye_size, eye_color, 1)

#dawing mouth based on user input using a custom arc function
mouth_color = drawly.terminal_input("Enter the color for the mouth: ")
drawly.terminal_output("NOTE! x/y Positions and size inputs are percentages of screen width/hight(0-100): x from left, y from bottom (0=bottom, 100=top).")
#mouth position
mouth_center_x = x_ratio(float(drawly.terminal_input("Enter the x-position for the mouth arc center (0-100): ")))
mouth_center_y = y_ratio(float(drawly.terminal_input("Enter the y-position for the mouth arc center (0-100): ")))
#size input
mouth_radius = size_ratio(float(drawly.terminal_input("Enter the width for the mouth arc: ")))
mouth_hight = size_ratio(float(drawly.terminal_input("Enter the hight for the mouth arc: ")))
mouth_thickness = int(drawly.terminal_input("Enter the line thickness for the mouth in pixels (0-100): "))
#streamlined native arc function arguments of starting and ending angle, combined into just "rotation"
mouth_rotation = int(drawly.terminal_input("Enter the rotation for the mouth in degrees (90=normal, increasing value=counterclockwise rotation): "))
draw_arc(mouth_color, mouth_center_x, mouth_center_y, mouth_radius, mouth_hight, mouth_rotation, mouth_thickness)

#Draw the user's name
drawly.set_color("black")
drawly.text(head_center_x, y_ratio(98), user_name, size_ratio(1))
drawly.draw()

drawly.done()