import turtle
import pandas
from writer import Writer

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.addshape(IMAGE)
screen.title("US States Game")
writer = Writer()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
turtle.shape(IMAGE)
correct_answers = 0

while correct_answers < 50:
    answer_state = screen.textinput(title="Guess the State",
                                    prompt=f"{correct_answers}/50 is Correct\nWhat's another state's name?", ).title()
    if answer_state == "Exit":
        break
    elif answer_state in states:
        correct_answers += 1
        states.remove(answer_state)
        writer.write_state(data, answer_state)

to_learn = pandas.DataFrame(states)
to_learn.to_csv("states_to_learn.csv")
