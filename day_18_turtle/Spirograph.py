from turtle import Turtle, Screen

tim = Turtle()

def main(size_of_gap):
    tim.speed("fastest")
    for _ in range(int(360/size_of_gap)):
        tim.circle(50)
        tim.right(50)





main(5)
screen = Screen()
screen.exitonclick()