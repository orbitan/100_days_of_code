from turtle import Turtle

import turtle as turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.shapesize(2)
        self.go_to_start_position()

    def move(self):
        self.forward(20)

    def go_to_start_position(self):
        self.goto(0, -270)
        self.setheading(90)
        self.showturtle()
