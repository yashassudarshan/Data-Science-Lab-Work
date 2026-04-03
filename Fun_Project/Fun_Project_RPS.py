import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Computer random choice
computer = random.choice(choices)

# User input
user = input("Enter rock, paper, or scissors: ").lower()

print("You chose:", user)
print("Computer chose:", computer)

# Determine winner
if user == computer:
    print("It's a tie!")

elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("Computer wins!")

elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("Computer wins!")

elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")

else:
    print("Invalid input! Please enter rock, paper, or scissors.")