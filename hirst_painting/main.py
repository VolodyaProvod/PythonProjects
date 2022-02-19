# import colorgram
# colors = colorgram.extract('image.jpg', 10)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
# print(rgb_colors)
from turtle import Turtle, Screen
from random import choice

rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
              (174, 94, 97), (176, 192, 209)]

tim = Turtle()
tim.penup()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
y = -300


def draw_circle():
    tim.color(choice(rgb_colors))
    tim.begin_fill()
    tim.circle(15)
    tim.end_fill()


def draw_line(y):
    x = -300
    for _ in range(10):
        tim.goto(x, y)
        draw_circle()
        x += 60


for _ in range(10):
    draw_line(y)
    y += 60

screen.exitonclick()