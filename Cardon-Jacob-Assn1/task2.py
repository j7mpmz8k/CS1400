import drawly

#window dimensions
x_pixels = 1920
y_pixels = 1080


#converts a position by percentage to pixel coordinate
def x_ratio(x_ratio):
    return x_pixels * x_ratio / 100
def y_ratio(y_ratio):
    return y_pixels*(100-y_ratio)/100

#used in snowball, puddle, buttons, eyes, and sun
def ball(x_ratio, y_ratio, size, fill="white", outline="black", outline_thickness=10):
    drawly.set_color(new_color=fill)
    drawly.circle(x_ratio, y_ratio, size)
    drawly.set_color(new_color=outline)
    drawly.circle(x_ratio, y_ratio, size, outline_thickness)

#used in hat, brim, cacti, and ground
def box(x_center, y_center, width, height, fill, outline="black", outline_thickness=5):
    drawly.set_color(new_color=fill)
    drawly.rectangle(x_center-(width/2), y_center-(height/2), width, height)
    drawly.set_color(new_color=outline)
    drawly.rectangle(x_center-(width/2), y_center-(height/2), width, height, outline_thickness)


#initialization
drawly.start("Bob in the desert", dimensions=(x_pixels, y_pixels), background="skyblue")
drawly.set_speed(speed=8)

#text labels
drawly.text(x_ratio(60), y_ratio(70), "Hi I'm Bob", 50) # optional font size
drawly.draw()

#ground
box(x_ratio(50), y_ratio(0), x_pixels, y_pixels*1.3, "peachpuff2", "gold")
#water puddle
ball(x_ratio(50),y_ratio(0),500, "blue", "skyblue")
ball(x_ratio(35),y_ratio(10),400, "blue", "skyblue")
drawly.draw()
ball(x_ratio(55),y_ratio(20),300, "blue", "skyblue")
ball(x_ratio(50),y_ratio(0),200, "blue", "skyblue")
drawly.draw()
ball(x_ratio(50),y_ratio(10),100, "blue", "skyblue")
drawly.draw()
#sun
ball(x_ratio(10),y_ratio(90),250, "yellow", "red", 20)
ball(x_ratio(10),y_ratio(90),200, "yellow", "orange", 20)
drawly.draw()
ball(x_ratio(10),y_ratio(90),150, "yellow", "gold", 20)
ball(x_ratio(10),y_ratio(90),100, "yellow", "gold", 20)
drawly.draw()
ball(x_ratio(10),y_ratio(90),50, "red", "white", 20)
drawly.draw()
#cacti
cacti_base_x = 10
cacti_base_y = 40
box(x_ratio(cacti_base_x), y_ratio(cacti_base_y), 40, 200, "darkgreen", "darkgreen")#stock
box(x_ratio(cacti_base_x+.4), y_ratio(cacti_base_y), 109, 30, "darkgreen", "darkgreen")#horizontal branch
drawly.draw()
box(x_ratio(cacti_base_x+2), y_ratio(cacti_base_y+5), 15, 80, "darkgreen", "darkgreen")#right branch
box(x_ratio(cacti_base_x+3), y_ratio(cacti_base_y+2), 10, 50, "darkgreen", "darkgreen")#second right branch
drawly.draw()
box(x_ratio(cacti_base_x-2), y_ratio(cacti_base_y+3), 15, 60, "darkgreen", "darkgreen")#left branch

#snowballs
ball(x_ratio(50),y_ratio(35),150)#bottom
ball(x_ratio(50),y_ratio(50),125)#torso
ball(x_ratio(50),y_ratio(65),100)#head
drawly.draw()
#buttons
ball(x_ratio(50),y_ratio(53),15, "brown", "brown")
ball(x_ratio(50),y_ratio(45),15, "brown", "brown")
ball(x_ratio(50),y_ratio(35),15, "brown", "brown")
drawly.draw()
#eyes
ball(x_ratio(48.5),y_ratio(67),10, "black")
ball(x_ratio(51.5),y_ratio(67),10, "black")
drawly.draw()
# Carrot nose
drawly.set_color("orange")
drawly.polygon_begin(stroke=0)  # Filled polygon, no outline
drawly.add_poly_point(x_ratio(60), y_ratio(64))  # tip of nose
drawly.add_poly_point(x_ratio(50), y_ratio(65))  # top of base
drawly.add_poly_point(x_ratio(50), y_ratio(63))  # bottom of base
drawly.polygon_end()
drawly.draw()
#mouth
drawly.set_color("pink")
drawly.line(x_ratio(47), y_ratio(60), x_ratio(53), y_ratio(61), 10)  # Slight slant for the mouth
drawly.draw()
# hat
box(x_ratio(50), y_ratio(80), 100, 80, "gold", "orange")#top
box(x_ratio(50), y_ratio(75), 150, 50, "gold", "orange")#brim
drawly.draw()


#left hand/arm
left_hand_base_x = 40
left_hand_base_y = 45
drawly.set_color("brown")
# Upper finger
drawly.line(x_ratio(left_hand_base_x), y_ratio(left_hand_base_y), x_ratio(left_hand_base_x - 2.5), y_ratio(left_hand_base_y + 2), 5)
# Middle finger
drawly.line(x_ratio(left_hand_base_x), y_ratio(left_hand_base_y), x_ratio(left_hand_base_x - 2.5), y_ratio(left_hand_base_y), 5)
# Lower finger
drawly.line(x_ratio(left_hand_base_x), y_ratio(left_hand_base_y), x_ratio(left_hand_base_x - 2.5), y_ratio(left_hand_base_y - 2), 5)
# Arm
drawly.set_color("brown")
drawly.line(x_ratio(left_hand_base_x+5), y_ratio(left_hand_base_y+5), x_ratio(left_hand_base_x), y_ratio(left_hand_base_y), 10)

#right hand/arm
right_hand_base_x = 60
right_hand_base_y = 45
# Upper finger
drawly.line(x_ratio(right_hand_base_x), y_ratio(right_hand_base_y), x_ratio(right_hand_base_x + 2.5), y_ratio(right_hand_base_y + 2), 5)
# Middle finger
drawly.line(x_ratio(right_hand_base_x), y_ratio(right_hand_base_y), x_ratio(right_hand_base_x + 2.5), y_ratio(right_hand_base_y), 5)
# Lower finger
drawly.line(x_ratio(right_hand_base_x), y_ratio(right_hand_base_y), x_ratio(right_hand_base_x + 2.5), y_ratio(right_hand_base_y - 2), 5)
# Arm
drawly.line(x_ratio(right_hand_base_x-5), y_ratio(right_hand_base_y+5), x_ratio(right_hand_base_x), y_ratio(right_hand_base_y), 10)
drawly.draw()

drawly.done()