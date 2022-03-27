from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RED_COLOR = "#ff5349"
GREEN_COLOR = "#0fff83"
FONT_TEXT = ("Arial", 18, "italic")
FONT_SCORE = ("Arial", 12, "bold")

class QuizUi:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizz_App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(fg="white", text="Score: 0", bg=THEME_COLOR, font=FONT_SCORE)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            font=FONT_TEXT,
            text="Some text here",
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next()

        self.window.mainloop()

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.window.after(1000, self.get_next)


    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have finished the test, congratulations!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
