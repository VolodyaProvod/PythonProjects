from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):

        self.cars = []
        self.car_speed = 0.1

    def add_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_x = 320
        new_y = randint(-240, 240)
        new_car.goto(new_x, new_y)
        new_car.color(choice(COLORS))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
            if car.xcor() <= -320:
                self.cars.remove(car)

    def generate_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            self.add_car()

    def clear_road(self):
        self.car_speed *= 0.9
