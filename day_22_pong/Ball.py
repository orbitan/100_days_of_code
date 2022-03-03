import random
import time
from turtle import Turtle

HEADINGS = [0, 360]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 4
        self.y_move = 4

    def move(self, heading):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1



