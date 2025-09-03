import drawly

drawly.start("My Drawing Program", background="light blue")

drawly.set_speed(speed=10)
drawly.set_color(new_color="white")

drawly.circle(600, 550, 150)

drawly.draw()

drawly.done()