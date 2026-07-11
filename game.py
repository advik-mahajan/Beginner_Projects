import random
game = random.choice(["stone", "paper", "scissor"])
while True:
    user = input("Enter your choice (enter quit to end the game): ").lower().strip()
    if user == "quit":
        break
    if user not in ["stone", "scissor", "paper"]:
        print("Enter a valid choice.")
        continue
    print(f"You chose {user}")
    print(f"Computer chose {game}")
    if user == game:
        print ("Tie!")
    elif game == "stone" and user == "paper":
        print("You Win!")
    elif game == "scissor" and user == "stone":
        print("You Win!")
    elif game == "paper" and user == "scissor":
        print("You Win!")
    else:
        print("You Lose!")
    choice = input("Do you want to play again? ").lower().strip()
    if choice == "yes" or "sure":
        game = random.choice(["stone", "paper", "scissor"])
        continue
    else:
        break





