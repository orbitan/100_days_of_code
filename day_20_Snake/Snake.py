import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if (self.head.heading()) != 270:
            self.head.setheading(90)

    def left(self):
        if (self.head.heading()) != 0:
            self.head.setheading(180)

    def right(self):
        if (self.head.heading()) != 180:
            self.head.setheading(0)

    def down(self):
        if (self.head.heading()) != 90:
            self.head.setheading(270)
