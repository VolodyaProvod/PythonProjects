rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock,paper,scissors]

import random
import os
clear = lambda: os.system('clear')



while True:
  clear()
  print("Hello! It's a rock/paper/scissors game, let's win a soulless computer!\n\n0 - rock\n1 - paper\n2 - scissors\n")
  player_number = int(input("> "))
  computer_choice = random.choice(choice_list)
  computer_number = choice_list.index(computer_choice)
  print(f"\nYour choice:\n{choice_list[player_number]}\n\nComputer choice:\n{computer_choice}\n")
  
  if player_number == 0:
    if computer_number == 0:
      print("You have a draw!")
    if computer_number == 1:
      print("You've lost!")
    if computer_number == 2:
      print("You've won!")

  if player_number == 1:
    if computer_number == 0:
      print("You've won!")
    if computer_number == 1:
      print("You have a draw!")
    if computer_number == 2:
      print("You've lost!")

  if player_number == 2:
    if computer_number == 0:
      print("You've lost!")
    if computer_number == 1:
      print("You've won!")
    if computer_number == 2:
      print("You have a draw!")
  
  continue_game = input("\nDo you want to play some more? 0 - I WANT MORE, 1 - exit\n>")
  if continue_game == "1":
    break
