import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pendown()
turtle.colormode(255)


#  List with all possible directions, colors, lenght
possible_routes = [['right', 'left'], ['green', 'red', 'blue', 'orange'], [30, 45, 60, 75, 90]]


def random_pace():
    r_pace = random.choice(possible_routes[2])
    return int(r_pace)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


def random_directory():
    poss = [True, False]
    r_directory = random.choice(poss)
    return r_directory

timmy.speed(100)
for _ in range(random.randint(1, 10000000)):
    timmy.pendown()
    timmy.pensize(15)
    pace = random_pace()
    timmy.color(random_color())
    color = turtle.pencolor(random_color()[0], random_color()[1], random_color()[2])
    direction = random_directory()
    if not random_directory():
        timmy.right(90)
    else:
        timmy.left(90)
    timmy.dot(15, random_color())
    timmy.forward(pace)



screen = Screen()
screen.exitonclick()
