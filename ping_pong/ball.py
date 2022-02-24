from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 5
        self.y_move = 5
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_speed = 0.04

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def check_collision_wall(self):
        if self.distance(self.xcor(), 300) < 12 or self.distance(self.xcor(), -300) < 12:
            return True
        return False

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.move_speed = 0.04
        self.setposition((0, 0))
        self.paddle_bounce()