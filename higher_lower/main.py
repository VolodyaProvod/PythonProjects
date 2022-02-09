from art import logo, vs
from game_data import data
from random import choice
from replit import clear

def take_data():
  return choice(data)

def check_answer(answer, A, B):
  if A['follower_count'] > B['follower_count'] and answer == "A":
    return True
  elif A['follower_count'] < B['follower_count'] and answer == "B":
    return True
  else:
    return False

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def game():
  game_status = True
  score = 0
  A = take_data()
  B = take_data()
  while game_status:
    print(logo)
    A = B
    while A == B:
      B = take_data()
    print(f"Compare A: {format_data(A)}\nFollowers - {A['follower_count']} millions")
    print(vs)
    print(f"Against B: {format_data(B)}")
    if check_answer(input("Who has more followers? Type 'A' or 'B': "), A, B):
        score += 1
        clear()
        print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong, {B['name']} has {B['follower_count']} millions subs. \nFinal score: {score}")
      game_status = False

game() 
