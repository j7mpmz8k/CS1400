# Jacob Cardon
# CS1400 - MWF - 8:30am
from drawly import *


class Moody:
    def __init__(self, start_smile, start_happy, start_dark_eyes):
        self.smile:bool = start_smile
        self.happy:bool = start_happy
        self.dark_eyes:bool = start_dark_eyes
        self.window_size:tuple[int,int] = (1280, 720)
        self.head_size: int = 400
        self.head_center_x = round(self.window_size[0] / 2)
        self.head_center_y = round(self.window_size[1] / 2)

    def draw_arc(self, center_x_pos, center_y_pos, width, height, color="black", rotation=0, thickness=5) -> None:
        """At 0 rotation: start angle is 180 and end angle adds 360 for a horizontally leveled arc."""
        radius = width/2
        set_color(color)
        arc(center_x_pos - radius, center_y_pos - radius, width, height, start=180+rotation, end=360+rotation, stroke=thickness)

    def is_smile(self)->bool:
        return self.smile
    def is_happy(self)->bool:
        return self.happy
    def is_dark_eyes(self)->bool:
        return self.dark_eyes

    def change_eyes(self)->None:
        self.dark_eyes = not self.dark_eyes
        self.draw_face()
    def change_mouth(self)->None:
        self.smile = not self.smile
        self.draw_face()
    def change_emotion(self)->None:
        self.happy = not self.happy
        self.draw_face()

    def draw_head(self)->None:
        set_color("black")
        circle(self.head_center_x, self.head_center_y, self.head_size // 2, 2)
        set_color("yellow") if self.happy else set_color("red")
        circle(self.head_center_x, self.head_center_y, self.head_size // 2)

    def draw_eyes(self)->None:
        radius = round(self.head_size * .10)
        center_y = self.head_center_y - round(self.head_size // 2 * .20)
        gap = round(self.head_size * .10)
        center_x_left = self.head_center_x - radius - gap
        center_x_right = self.head_center_x + radius + gap
        set_color("black") if self.dark_eyes else set_color("green")
        circle(center_x_left, center_y, radius)
        circle(center_x_right, center_y, radius)

    def draw_mouth(self)->None:
        width = round(self.head_size * .60)
        height = round(self.head_size * .40)
        y_modifier = 0 if self.smile else height // 2
        center_y = self.head_center_y + round(self.head_size // 2 * .80) - height // 2 + y_modifier
        rotation = 0 if self.smile else 180
        self.draw_arc(self.head_center_x, center_y, width, height, rotation=rotation)

    def draw_face(self)->None:
        self.draw_head()
        self.draw_eyes()
        self.draw_mouth()
        drawly.redraw()
