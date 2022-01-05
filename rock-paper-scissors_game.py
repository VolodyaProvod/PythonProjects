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
  
  if player_number == computer_number:
  	print("You have a draw!")
  elif (player_number == 0 and computer_number == 2) or (player_number == 1 and computer_number == 0) or (player_number == 2 and computer_number == 1):
  	print("You've won!")
  else:
      print("You've lost!")
  
  continue_game = input("\nDo you want to play some more? 0 - I WANT MORE, 1 - exit\n>")
  if continue_game == "1":
    break