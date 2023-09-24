# Game: Higher or Lower?
from art import logo, vs
import os #it helps cleaning the previous stage
from game_data import data 
import random 

#Function to select a random person from the dictionary
def select_person():
  """Select a Random Person"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  # Values from the Keys in the person_a
  person_name = account["name"]
  profesion = account["description"]
  person_country = account["country"]
  return f"{person_name}, a {profesion}, from {person_country}"

def check_answer(guess, person_a, person_b):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if person_a > person_b:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  person_a = select_person()
  person_b = select_person()

  while game_should_continue:
    person_a = person_b
    person_b = select_person()

    while person_a == person_b:
      person_b = select_person()

    print(f"Compare A: {format_data(person_a)}.")
    print(vs)
    print(f"Against B: {format_data(person_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = person_a["follower_count"]
    b_follower_count = person_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls' if os.name == 'nt' else 'clear') #with this code the game would clean the previous stage
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()