letter_layout = ""
with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    letter_layout = file.read()

list_names = []
with open("./Input/Names/invited_names.txt", mode="r") as file:
    list_names = file.readlines()

for name in list_names:
    clear_name = name.strip("\n")
    with open(f"./Output/ReadyToSend/Letter_for_{clear_name}.txt", mode="w") as file:
        letter = letter_layout.replace("[name]", clear_name)
        file.write(letter)