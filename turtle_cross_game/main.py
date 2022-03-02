import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
cars_control = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars_control.car_speed)
    cars_control.generate_cars()
    cars_control.move()

    if turtle.is_finish():
        scoreboard.write_level()
        cars_control.clear_road()

    for car in cars_control.cars:
        if turtle.distance(car) < 18:
            scoreboard.end_game()
            game_is_on = False

    screen.update()

screen.exitonclick()