import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280, 281)
        random_y = random.randint(-280, 281)
        self.penup()
        self.goto(random_x, random_y)

    def refresh(self):
        self.hideturtle()
        random_x = random.choice(range(-280, 280, 20))
        random_y = random.choice(range(-280, 280, 20))
        self.goto(random_x, random_y)
        self.showturtle()
