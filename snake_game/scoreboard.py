from turtle import Turtle
SCORE_COORDINATES = (0, 250)
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_COORDINATES)
        self.color("white")
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
