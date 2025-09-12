# Jacob Cardon
# CS1400 - MWF - 8:30am

import drawly

# #window dimensions...common 16:9 ratios: 3840X2160, 2560X1440, 1920x1080, 1280x720(default), 854X480, 640x360
x_pixels = 1920
y_pixels = 1080

# Converts a position by percentage to pixel coordinate (y inverted for top-left origin)
def x_ratio(x_ratio):
    return x_pixels * x_ratio / 100

def y_ratio(y_ratio):
    return y_pixels * (100 - y_ratio) / 100

# Converts a size by percentage to pixel value, using window width for scaling
def size_ratio(size_ratio):
    return x_pixels * size_ratio / 100

# Function to draw a filled circle with an optional outline for easier rendering of circular elements like the head and eyes.
def ball(x, y, radius, fill="white", outline="black", outline_thickness=0):
    drawly.set_color(fill)
    drawly.circle(x, y, radius)
    if outline_thickness > 0:
        drawly.set_color(outline)
        drawly.circle(x, y, radius, outline_thickness)

# Display a welcome message to the user in the IDE terminal, as it precedes window initialization.
print("Welcome to the Faceinator program. This application will guide you through creating a customized face drawing based on your inputs.")

# Prompt the user for their name using standard input, as required before initializing the Drawly window.
user_name = input("Please enter your name: ")

# Initialize the Drawly graphics window with a title incorporating the user's name, specified dimensions for scaling,
# and the terminal enabled for subsequent interactions.
drawly.start(title=f"{user_name}'s Faceinator", dimensions=(x_pixels, y_pixels), terminal=True)

# Clear the terminal for a clean start after initialization.
drawly.terminal_clear()

# Output informational message to the Drawly terminal and gather input for the head.
drawly.terminal_output("Next, provide details for the head. Positions are percentages (0-100): x from left, y from bottom (0=bottom, 100=top). Sizes are percentages of window width.")
head_center_x = x_ratio(float(drawly.terminal_input("Enter the x-percentage for the center of the head (0-100): ")))
head_center_y = y_ratio(float(drawly.terminal_input("Enter the y-percentage for the center of the head (0-100): ")))
head_radius = size_ratio(float(drawly.terminal_input("Enter the radius percentage for the head (e.g., 10 for 10% of width): ")))
head_color = drawly.terminal_input("Enter the color for the head (e.g., yellow): ")

# Draw the head using the ball function with an outline for enhanced definition.
ball(head_center_x, head_center_y, head_radius, fill=head_color, outline="black", outline_thickness=2)
drawly.draw()

# Output informational message to the Drawly terminal and gather input for the eyes.
drawly.terminal_output("Next, provide details for the eyes. Positions are percentages (0-100): x from left, y from bottom (0=bottom, 100=top).")
eye_color = drawly.terminal_input("Enter the color for both eyes (e.g., blue): ")
left_eye_x = x_ratio(float(drawly.terminal_input("Enter the x-percentage for the left eye (0-100): ")))
left_eye_y = y_ratio(float(drawly.terminal_input("Enter the y-percentage for the left eye (0-100): ")))
left_eye_size = size_ratio(float(drawly.terminal_input("Enter the size percentage for the left eye (0-100): ")))
right_eye_x = x_ratio(float(drawly.terminal_input("Enter the x-percentage for the right eye (0-100): ")))
right_eye_y = y_ratio(float(drawly.terminal_input("Enter the y-percentage for the right eye (0-100): ")))
right_eye_size = size_ratio(float(drawly.terminal_input("Enter the size percentage for the right eye (0-100): ")))


# Draw the left and right eyes using the ball function (with optional thin outline for subtle definition).
ball(left_eye_x, left_eye_y, left_eye_size, fill=eye_color, outline="black", outline_thickness=1)
drawly.draw()
ball(right_eye_x, right_eye_y, right_eye_size, fill=eye_color, outline="black", outline_thickness=1)
drawly.draw()

# Output informational message to the Drawly terminal and gather input for the mouth, implemented as an arc.
drawly.terminal_output("Next, provide details for the mouth, which will be drawn as an arc. Positions are percentages (0-100): x from left, y from bottom (0=bottom, 100=top). Radius is percentage of window width.")
mouth_color = drawly.terminal_input("Enter the color for the mouth (e.g., red): ")
mouth_thickness = int(drawly.terminal_input("Enter the line thickness for the mouth in pixels: "))
mouth_center_x = x_ratio(float(drawly.terminal_input("Enter the x-percentage for the mouth arc center (0-100): ")))
mouth_center_y = y_ratio(float(drawly.terminal_input("Enter the y-percentage for the mouth arc center (0-100): ")))
mouth_radius = size_ratio(float(drawly.terminal_input("Enter the radius percentage for the mouth arc (e.g., 8): ")))
mouth_start_angle = int(drawly.terminal_input("Enter the starting angle for the mouth arc in degrees (e.g., 180): "))
mouth_end_angle = int(drawly.terminal_input("Enter the ending angle for the mouth arc in degrees (e.g., 180): "))

# Draw the mouth arc, adjusting for the bounding rectangle of the arc function.
drawly.set_color(mouth_color)
drawly.arc(mouth_center_x - mouth_radius, mouth_center_y - mouth_radius, 2 * mouth_radius, 2 * mouth_radius,
           mouth_start_angle, mouth_end_angle, mouth_thickness)
drawly.draw()

# Position the name approximately 2% of window width below the head bottom for scalability.
name_offset = float(size_ratio(2.0))  # Scalable offset approximating 25 pixels at standard resolution.
name_y = head_center_y + head_radius + name_offset
name_font_size = int(size_ratio(1.0))  # Scalable font size approximating 20 pixels.

# Draw the user's name without centering.
drawly.set_color("black")
drawly.text(head_center_x, name_y, user_name, name_font_size)
drawly.draw()

# Display a thank-you message to the user in the Drawly terminal.
drawly.terminal_output("Thank you for using the Faceinator program. The drawing is complete. You may close the graphics window to exit.")

# Finalize the drawing and keep the window open until closed by the user.
drawly.done()