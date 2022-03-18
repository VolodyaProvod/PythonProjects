from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
words_to_learn = {}

# ---------------------------- Work with data ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/russian_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer, words_to_learn
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(language_title, text="Russian", fill="black")
    canvas.itemconfig(word_to_translate, text=current_card["Russian"], fill="black")
    canvas.itemconfig(main_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_title, text="English", fill="white")
    canvas.itemconfig(word_to_translate, text=current_card["English"], fill="white")
    canvas.itemconfig(main_image, image=card_back_image)


def remove_word():
    global current_card, words_to_learn
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def add_to_learn():
    global current_card
    words_to_learn.update(current_card)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

# Create Window

window = Tk()
window.title("Translate Game")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Create Canvas with Image and titles
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
main_image = canvas.create_image(400, 263, image=card_front_image)
language_title = canvas.create_text(400, 150, font=LANGUAGE_FONT)
word_to_translate = canvas.create_text(400, 263, font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Create Buttons

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
