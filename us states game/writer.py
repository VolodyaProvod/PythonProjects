from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, data, state):
        new_x = int(data[data.state == state]["x"])
        new_y = int(data[data.state == state]["y"])
        self.goto(new_x, new_y)
        print(state)
        self.write(state, False, font=FONT)
