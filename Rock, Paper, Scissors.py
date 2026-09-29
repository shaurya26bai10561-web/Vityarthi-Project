import random

print("================================")
print("  Welcome to Rock Paper Scissors!")
print("================================")
print("Let's start the game!\n")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if user == "quit":
        print("\nThanks for playing! Goodbye!")
        break

    if user not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")

    else:
        print("Computer wins!")

    print("--------------------------------\n")