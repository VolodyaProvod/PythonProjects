from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.listen()


def write_dash(line, times):
    line.pendown()
    for _ in range(times):
        line.forward(15)
        line.penup()
        line.forward(15)
        line.pendown()


dashed_line = Turtle()
dashed_line.penup()
dashed_line.hideturtle()
dashed_line.color("white")
dashed_line.goto(0, -300)
dashed_line.setheading(90)
write_dash(dashed_line, 20)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
ball.speed("fastest")
scoreboard = ScoreBoard()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check collision with wall
    if ball.check_collision_wall():
        ball.wall_bounce()

    # check collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    # check right player miss
    if ball.xcor() > 400:
        ball.restart()
        scoreboard.l_goal()

    # check left player miss
    if ball.xcor() < -400:
        ball.restart()
        scoreboard.r_goal()

    # check left player wins
    if scoreboard.l_score == 7:
        scoreboard.l_wins()
        game_is_on = False

    # check right player wins

    if scoreboard.r_score == 7:
        scoreboard.r_wins()
        game_is_on = False

screen.exitonclick()
