import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["green", "blue", "red", "yellow", "purple"]


def position(i):
    x = -200
    y = -115 + (i * 400 // len(colors))
    return x, y


i = 0
for el in colors:
    t = Turtle(shape="turtle")
    t.shapesize(2)
    t.penup()
    t.color(el)
    posx = position(i)[0]
    posy = position(i)[1]
    t.goto(posx, posy)
    i += 1

screen.exitonclick()
