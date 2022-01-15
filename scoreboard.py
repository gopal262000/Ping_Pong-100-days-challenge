from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 210)
        self.write(
            f"{self.l_score}", True, align=ALIGNMENT, font=FONT)
        self.goto(100, 210)
        self.write(
            f"{self.r_score}", True, align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
