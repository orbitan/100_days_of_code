from turtle import Turtle
import pandas

ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.f = open("high_score.csv", "r")
        for last_line in self.f:
            pass
        self.high_score = int(last_line)
        self.f.close()
        self.score = 0
        self.text = f"Score: {self.score} Highscore: {self.high_score}"
        self.color("white")

        self.penup()
        self.display_score()

    def display_score(self):
        self.clear()
        self.setposition(0, 275)
        self.write(f"Score {self.score} Highscore {self.high_score}", move=False, align=ALIGNMENT,
                   font=("Calibri", 15, "bold"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=("Calibri", 15, "bold"))
        f = open("high_score.csv", "w")
        f.write(str(self.high_score))

        f.close()

    def set_score(self):
        self.score += 1
        self.set_high_score()
        self.display_score()

    def set_high_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score



