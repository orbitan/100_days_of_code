import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
race = True
turtle_list = []
colors = ["blue", "red", "green", "purple"]

guess = screen.textinput("hi", "Make a guess: \n"
                               "Who will win the game?")


def create_turtle():
    i = 0
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.shapesize(2)
        new_turtle.color(colors[colors.index(color)])
        new_turtle.penup()

        new_turtle.setx(-200)
        new_turtle.sety(set_coordinates(4, i))
        i += 1

        turtle_list.append(new_turtle)


def set_coordinates(am_turtles, i):
    y_help = 400 - (2 * am_turtles + (am_turtles - 1) + i * 200)
    y = y_help // 2 - 40
    return y


def winner(winning_color):
    print(winning_color)
    for turtle in turtle_list:
        turtle.hideturtle()

    if guess == winning_color:
        print(f"{winning_color} won. You won.")
    else:
        print(f"{winning_color} won. You lose.")

    screen.textinput(f"{winning_color} won. Another ruound?", "h")


def forwards():
    global race
    target = 220
    while race:
        for new_turtle in turtle_list:
            x = new_turtle.xcor() + random.randint(1, 11)
            new_turtle.setx(x)
            if x > target:
                winner_color = turtle_list.index(new_turtle)
                winner(colors[winner_color])
                race = False


def main_loop():
    create_turtle()
    while race:
        forwards()


main_loop()

screen.exitonclick()
