from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

DEFAULT_EMAIL = "achapovsky@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_input.delete(0, END)
    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = letters_list + symbols_list + number_list

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oooops", message="Data file is not exist")
    else:
        if website in data:
            email = data[f"{website}"]["email"]
            password = data[f"{website}"]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Oooops", message="Password for this site is not created!")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    mail = mail_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": mail,
            "password": password
        }
    }

    is_empty = len(website) == 0 or len(mail) == 0 or len(password) == 0
    if is_empty:
        messagebox.showinfo(title="Oooops", message="All fields must be filled in!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Create Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=40)

# Create Canvas with Image
canvas = Canvas(width=200, height=189)
main_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=main_image)
canvas.grid(row=0, column=1)

# Create Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Create Inputs

website_input = Entry(width=32)
website_input.focus()
website_input.grid(row=1, column=1)
mail_input = Entry(width=51)
mail_input.insert(0, DEFAULT_EMAIL)
mail_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=32)
password_input.grid(row=3, column=1)

# Create Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
