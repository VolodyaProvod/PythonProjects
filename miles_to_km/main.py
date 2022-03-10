from tkinter import *


def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609344, 2)
    calc_km.config(text=f"{km}")


window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

text = Label(text="is equal to", font=("Times new roman", 12, "normal"))
text.grid(row=1, column=0)

calc_km = Label(text="0", font=("Times new roman", 12, "normal"))
calc_km.grid(row=1, column=1)

km = Label(text="Km", font=("Times new roman", 12, "normal"))
km.grid(row=1, column=2)

ml = Label(text="Miles", font=("Times new roman", 12, "normal"))
ml.grid(row=0, column=2)

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(row=2, column=1)

input = Entry(font=("Times new roman", 12, "normal"), width=8)
input.insert(END, string="0")
input.grid(row=0, column=1)

window.mainloop()
