import time
import turtle
from turtle import Screen, Turtle

# Snake
from day_20_Snake.Food import Food
from day_20_Snake.Score import Score
from day_20_Snake.Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(2)

snake = Snake()

food = Food()
food.refresh()
score = Score()

screen.listen()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    screen.onkey(snake.up, 'w')
    screen.onkey(snake.left, 'a')
    screen.onkey(snake.right, 'd')
    screen.onkey(snake.down, 's')
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.set_score()
        snake.extend()

    #  Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_is_on = False

    #  Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

if not game_is_on:
    score.game_over()


screen.exitonclick()
