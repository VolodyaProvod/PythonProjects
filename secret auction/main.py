from replit import clear
from art import logo

print(logo)
print("Hi, it's a Secret Auction Program! Now we will decide which of you is willing to pay more!")

participants = {}
action = True

def find_highest(bidder):
  max_cost = 0
  winner_name = ""
  for bid in participants:
    if participants[bid] > max_cost:
      winner_name = bid
      max_cost = participants[bid]
  print(f"The winner is a {winner_name} with a bid of ${max_cost}") 

while action:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  participants[name] = bid
  need_to_continue = input("Are there any other bidders? Type 'yes' or 'no' \n")
  clear()
  if need_to_continue == "no":
    action = False
    find_highest(participants)