#Rock Paper Scissors Game

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        user_choice = user_choice.lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

print("Welcome to Rock-Paper-Scissors!")
print("Enter 'rock', 'paper', or 'scissors' to make your choice.")
play_game()

