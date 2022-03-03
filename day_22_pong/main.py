import time
from turtle import Turtle, Screen
from Paddle import *
from Ball import *
from Score_Board import *

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_left = Paddle("left")
paddle_right = Paddle("right")
ball = Ball()
score = Score()
score.display_score()

game_is_on = True

screen.listen()
heading = random.randint(0, 360)
ball.move(heading)
time_sleep = 0.01
while game_is_on:
    screen.update()
    time.sleep(time_sleep)
    ball.move(heading)

    #  Move paddles
    screen.onkey(paddle_left.up, 'w')
    screen.onkey(paddle_right.up, 'Up')
    screen.onkey(paddle_left.down, 's')
    screen.onkey(paddle_right.down, 'Down')

    #  Detect collision with paddle
    prc = paddle_right.paddle_segments[2].ycor()
    plc = paddle_left.paddle_segments[2].ycor()

    #  Right
    if ball.xcor() > 360 and prc - 60 < ball.ycor() < prc + 60:
        ball.paddle_bounce()
        score.set_score("right")
    #  Left
    elif ball.xcor() < -370 and plc - 60 < ball.ycor() < plc + 60:
        ball.paddle_bounce()
        score.set_score("left")

    #  Detect collision with frame
    #  Up
    if int(ball.ycor()) >= 270:
        ball.bounce()

    #  Down
    if int(ball.ycor()) <= -270:
        ball.bounce()

    # Detect collision with frame left/right
    if int(ball.xcor()) >= 380:
        game_is_on = False

    elif int(ball.xcor()) <= -380:
        game_is_on = False

    if not game_is_on:
        score.game_over()

screen.exitonclick()
