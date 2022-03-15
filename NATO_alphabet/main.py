import pandas

alphabet = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}


def generate_phonetic():
    name = input("Input your name: ").upper()
    try:
        nato_format = [alphabet[letter] for letter in name]
    except KeyError:
        print("Input your name in the correct form")
        generate_phonetic()
    else:
        print(f"Your name in NATO format: {nato_format}")


generate_phonetic()
