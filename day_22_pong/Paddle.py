from turtle import Turtle

PADDLE_POSITIONS = [-40, -20, 0, 20, 40]


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.paddle_segments = []
        self.create_paddle()
        self.coordinate = self.paddle_segments[0].ycor()

    def create_paddle(self):
        for i in range(5):
            new_segment = Turtle("square")
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            if self.side == "right":
                x = 375
                new_segment.goto(x, PADDLE_POSITIONS[i])
                self.paddle_segments.append(new_segment)
            else:
                x = -375
                new_segment.goto(x, PADDLE_POSITIONS[i])
                self.paddle_segments.append(new_segment)

    def up(self):
        for i in range(len(self.paddle_segments)):
            new_x = self.paddle_segments[i].xcor()
            new_y = self.paddle_segments[i].ycor() + 20
            self.paddle_segments[i].goto(new_x, new_y)


    def down(self):
        for i in range(len(self.paddle_segments)):
            new_x = self.paddle_segments[i].xcor()
            new_y = self.paddle_segments[i].ycor() - 20
            self.paddle_segments[i].goto(new_x, new_y)
