############### Blackjack Project #####################

import random
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(hand):
  if len(hand) == 2 and sum(hand) == 21:
    return 0
  elif 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return sum(hand)

from replit import clear

def play():
  clear()
  print(logo)
  user = []
  computer = []
  game_active = True

  for _ in range(0,2):
    user.append(deal_card())
    computer.append(deal_card())
  
  while game_active:
    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computers first card: {computer[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_active = False
    else:
      if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        user.append(deal_card())
      else:
        game_active = False
  
  while computer_score < 17 and computer_score != 0 and user_score < 21:
    computer.append(deal_card())
    computer_score = calculate_score(computer)
  
  print(f"Your cards: {user}, final score: {user_score}")
  print(f"Computer cards: {computer}, final score: {computer_score}")

  print(compare(user_score, computer_score))


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win, you have Blackjack"
  elif user_score > 21:
    return "You Loose..."
  elif computer_score > 21:
    return "You Win!"
  elif computer_score < user_score:
    return "You win!"
  elif computer_score > user_score:
    return "You Loose...!"

while input("Do you want to play again? Type 'y' or 'n': ") == "y":
  play()