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

    def __draw_arc(self, center_x_pos, center_y_pos, width, height, color="black", rotation=0, thickness=10) -> None:
        """
        Helper method for draw_mouth()
        At 0 rotation: start angle is 180 and end angle adds 360 for a horizontally leveled arc.
        """
        radius = width/2
        set_color(color)
        arc(center_x_pos - radius, center_y_pos - height / 2, width, height, start=180+rotation, end=360+rotation, stroke=thickness)

    def is_smile(self)->bool:
        return self.smile
    def is_happy(self)->bool:
        return self.happy
    def is_dark_eyes(self)->bool:
        return self.dark_eyes

    def change_eyes(self)->None:
        """flips between green and black eyes"""
        self.dark_eyes = not self.dark_eyes
        self.draw_face()
    def change_mouth(self)->None:
        """flips between smiling and frowning"""
        self.smile = not self.smile
        self.draw_face()
    def change_emotion(self)->None:
        """flips between happy and mad"""
        self.happy = not self.happy
        self.draw_face()

    def draw_head(self)->None:
        """
        draws circle with black outline.
        Yellow fill if happy, red fill if not happy.
        """
        set_color("yellow") if self.happy else set_color("red")
        circle(self.head_center_x, self.head_center_y, self.head_size // 2)
        set_color("black")
        circle(self.head_center_x, self.head_center_y, self.head_size // 2, 5)

    def draw_eyes(self)->None:
        """
        draws two circles based on head position with relative gap between them.
        Black fill if dark eyes, green fill if not dark eyes.
        """
        radius = round(self.head_size * .10)
        center_y = self.head_center_y - self.head_size // 10
        gap = round(self.head_size * .10)
        center_x_left = self.head_center_x - gap - radius
        center_x_right = self.head_center_x + gap + radius
        set_color("black") if self.dark_eyes else set_color("green")
        circle(center_x_left, center_y, radius)
        circle(center_x_right, center_y, radius)

    def draw_mouth(self)->None:
        """
        calls draw_arc() helper method to draw smille for easier rotation management.
        0 rotation is smiling, 180 is frowning
        dimensions and position are based on head attributes
        """
        width = round(self.head_size * .60)
        height = round(self.head_size * .40)
        y_modifier = 0 if self.smile else height // 2# used since smile flips by x axis at top of smile when rotation is 180
        center_y = self.head_center_y + round(self.head_size // 2 * .70) - height // 2 + y_modifier
        rotation = 0 if self.smile else 180
        self.__draw_arc(self.head_center_x, center_y, width, height, rotation=rotation)

    def draw_face(self)->None:
        self.draw_head()
        self.draw_eyes()
        self.draw_mouth()
        drawly.redraw()
