# Import the random module
import random

# Define the choices for the game
choices = ["rock", "paper", "scissors"]

# Define the rules for winning
rules = {
  "rock": "scissors",
  "paper": "rock",
  "scissors": "paper"
}

# Initialize the score for both the user and the computer
user_score = 0
computer_score = 0

# Use a while loop to keep the game running
while True:
  # Print a welcome message and the current score
  print("Welcome to the rock, paper, scissors game!")
  print(f"Your score: {user_score}")
  print(f"Computer's score: {computer_score}")

  # Ask the user for their choice
  user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ")

  # If the user enters 'q', break the loop and end the game
  if user_choice == "q":
    print("Thanks for playing!")
    break

  # If the user enters an invalid choice, print an error message and continue the loop
  if user_choice not in choices:
    print("Invalid choice. Please try again.")
    continue

  # Generate the computer's choice using the random module
  computer_choice = random.choice(choices)

  # Print the user's and the computer's choices
  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")

  # Compare the user's and the computer's choices and determine the winner
  # If the user and the computer have the same choice, it is a tie
  if user_choice == computer_choice:
    print("It's a tie!")
  # If the user's choice beats the computer's choice, the user wins
  elif rules[user_choice] == computer_choice:
    print("You win!")
    # Increment the user's score by 1
    user_score += 1
  # Otherwise, the computer wins
  else:
    print("You lose!")
    # Increment the computer's score by 1
    computer_score += 1

  # Print a blank line for spacing
  print()