# number guessing game

import random

logo = """
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \\
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/

"""
print(logo)

def number_guessing_game():
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  print("Can you guess what it is?")

  answer = random.randint(1, 100)
  lives = set_difficulty()

  while lives > 0 :  
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  
    lives = check_answer(guess, answer, lives)
    if lives == 0 and guess != answer:
        print("You've run out of guesses, you lose.")
        print(f"The answer was {answer}.")
        break
    elif guess == answer:
        break
    else:
        print(f"You have {lives} attempts remaining to guess the number.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  else:
      print("Invalid input. Setting difficulty to 'easy' by default.")
      return 10

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
      print(f"You got it! The answer was {answer}.")
      return 0

if __name__ == "__main__":
   number_guessing_game()





  