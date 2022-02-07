from art import logo
import random

def complexity():
  if input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
    return 5
  else:
    return 10

def choice_random():
  return random.randint(1, 100)

def greeting():
  print (logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

def check_answer(num_user, num_computer, difficulty):
  if num_user > num_computer:
    print("Too high.")
    return difficulty - 1
  elif num_user < num_computer:
    print("Too low.")
    return difficulty - 1
  else:
    print(f"You got it 😊! The answer was {num_computer}.")

def game():
  greeting()
  difficulty = complexity()
  random_number = choice_random()
  user_nubmer = 0

  while user_nubmer != random_number:
    print(f"You have {difficulty} attempts remaining to guess the number.")
    user_nubmer = int(input("Make a guess: "))
    difficulty = check_answer(user_nubmer, random_number, difficulty)
    if (difficulty == 0):
      print(f"You've run out of guesses, you lose 😞. The answer was {random_number}")
      return
    elif user_nubmer != random_number:
      print("Guess again.")

game()