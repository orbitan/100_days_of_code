from turtle import Turtle

ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.text = f"{self.score_left} : {self.score_right} "
        self.color("white")

        self.penup()
        self.display_score()

    def display_score(self):
        self.clear()
        self.setposition(0, 275)
        self.write(f"{self.score_left}: {self.score_right}", move=False, align=ALIGNMENT, font=("Calibri", 15, "bold"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=("Calibri", 15, "bold"))

    def set_score(self, side):
        if side == "left":
            self.score_left += 1
        elif side == "right":
            self.score_right += 1
        self.display_score()

