from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 250)
        self.write_level()

    def write_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
