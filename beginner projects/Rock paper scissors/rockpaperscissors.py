import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Please enter your choice (rock/paper/scissors): ").lower()

    if user_choice in options:
        computer_choice = random.choice(options)
        print("You chose: ", user_choice)
        print("Computer chose: ", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "quit":
        break
    else:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
