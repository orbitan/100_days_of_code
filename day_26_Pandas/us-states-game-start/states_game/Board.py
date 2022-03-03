from turtle import *


class Board(Turtle):
    def __init__(self, play_map):
        super().__init__()
        self.play_map = play_map
        self.hideturtle()

    def set_screen(self, screen):
        image = f"blank_maps/{self.play_map}.gif"
        screen.bgpic(image)
