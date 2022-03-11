from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LABEL_FONT = ("Courier", 35, "bold")
TIMER_FONT = ("Courier", 25, "bold")
CHECKMARK_FONT = ("Courier", 18, "bold")
BUTTON_FONT = ("Arial", 8, "normal")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="0:00")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        header.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        header.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        header.config(text="Timer", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.trunc(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.trunc(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#Create Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#Create Header Lable
header = Label(text="Timer", font=LABEL_FONT, fg=GREEN, bg=YELLOW)
header.grid(row=0, column=1)

#Create Canvas with Image and Text
canvas = Canvas(width=202, height=234, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
main_image = canvas.create_image(101, 117, image=tomato_image)
timer_text = canvas.create_text(102, 140, text="0:00", fill="white", font=TIMER_FONT)
canvas.grid(row=1, column=1)

#Create Button Start
start_button = Button(text="Start", bg="white", width=8, font=BUTTON_FONT, command=start_timer)
start_button.grid(row=2, column=0)

#Create Button Reset
reset_button = Button(text="Reset", bg="white", width=8, font=BUTTON_FONT, command=reset_timer)
reset_button.grid(row=2, column=2)

#Create CheckMark
checkmark = Label(font=CHECKMARK_FONT, fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)



window.mainloop()
