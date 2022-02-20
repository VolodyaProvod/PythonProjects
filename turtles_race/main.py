from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-100, -58, -16, 26, 68, 110]
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[i])
    new_turtle.color(colors[i])
    turtles.append(new_turtle)

if user_bet in colors:
    race_is_on = True


while race_is_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've loose! The {winning_color} is the winner")
            race_is_on = False
            break

screen.exitonclick()
