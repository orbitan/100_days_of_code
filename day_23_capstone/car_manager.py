import random
from turtle import Turtle


import numpy as np
import numpy.random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.drive_distance = -2

        self.hideturtle()
        self.cars = []
        self.distance = 0

    def create_car(self):
        new_car = Turtle("square")
        new_car.hideturtle()
        new_car.penup()

        new_car_x = random.randint(260, 600)
        new_car_y = random.randint(-260, 280)
        new_car.setposition(new_car_x, new_car_y)
        new_car.showturtle()
        new_car.penup()

        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        self.cars.append(new_car)

    def move_cars(self, distance):
        for i in range(len(self.cars)):
            self.cars[i].forward(distance)

