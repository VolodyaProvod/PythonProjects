from replit import clear
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo + "\n")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f"You already input {guess}, try again")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(f"{''.join(display)}")

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"Uppss, letter {guess} is not in word, you lose live")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe right word is {chosen_word}")

   

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    print(hangman_art.stages[lives])