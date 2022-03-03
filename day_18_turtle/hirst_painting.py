from turtle import Turtle, Screen
import random

extracted_colors = [(221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]

#  10 x 10
#  Radius = 20
#  Space = 50

TURTLE_SIZE = 20

screen = Screen()
size = 10*20+10*50
screen.setup(size, size)
screen.colormode(255)


yertle = Turtle(shape="turtle", visible=False)
yertle.penup()
yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2 + 100, - (screen.window_height()/2) + TURTLE_SIZE + 100)
yertle.pendown()
yertle.showturtle()


space = 50
radius = 20
amount = 10


def direction(i):
    if i%2 == 0:
        yertle.left(90)
    else:
        yertle.right(90)


def draw_dots():
    i = -1
    yertle.penup()
    for column in range(10):
        i += 1
        for _ in range(9):
            yertle.dot(radius, random.choice(extracted_colors))
            yertle.forward(50)
        direction(i)
        yertle.dot(radius)
        yertle.forward(50)
        direction(i)



draw_dots()
yertle.hideturtle()


screen.exitonclick()
