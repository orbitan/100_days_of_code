import time

from Board import *
from PlayBoard import *

screen = turtle.Screen()
turtle.hideturtle()
turtle.penup()
screen.title(f"States")
play_map = screen.textinput(title="Map", prompt="USA or Germany?")
screen.exitonclick()

if play_map == "USA":
    a = Board("united_states")
    p = PlayBoard("united_states")
else:
    a = Board("germany")
    p = PlayBoard("germany")

a.set_screen(screen)

while True:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state?")
    if answer_state is None:
        p.exit()
        time.sleep(20)
        quit()

    p.proceed_data(answer_state)



