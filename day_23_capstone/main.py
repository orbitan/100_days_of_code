import time
from turtle import Screen
from car_manager import *
from day_23_capstone.scoreboard import Scoreboard

from player import *

CHANCE_TO_SPAWN_CAR = 0.01

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(2)
cars = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
target = Turtle()
target.penup()
target.color("red")
target.setx(-300)
target.sety(260)
target.setheading(0)
target.pensize(5)
target.pendown()
target.forward(600)
score.display_score()
game_is_on = True

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
PROBABILITY_TRUE = 0.01
PROBABILITY_FALSE = 0.99


distance = -5
while game_is_on:
    screen.update()
    time.sleep(0.01)

    draw = numpy.random.choice([True, False], p=[PROBABILITY_TRUE, PROBABILITY_FALSE])
    if draw:
        cars.create_car()
    cars.move_cars(distance)
    screen.onkey(player.move, "w" or "Up")

    for car in cars.cars:
        if -20 <= car.pos()[0] <= 20 and car.pos()[1] - 20 <= player.pos()[1] <= car.pos()[1]:
            game_is_on = False

    if 240 <= player.pos()[1] <= 260:
        print("Win")
        score.set_score()
        player.go_to_start_position()
        distance -= 5
        PROBABILITY_TRUE += 0.1
        PROBABILITY_FALSE -= 0.1

if not game_is_on:
    print("Game over my lil peace a shit")

screen.exitonclick()
