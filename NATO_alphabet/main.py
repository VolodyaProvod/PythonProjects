import pandas

alphabet = {row.letter: row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
name = input("Input your name: ").upper()
nato_format = [alphabet[letter] for letter in name]
print(nato_format)
