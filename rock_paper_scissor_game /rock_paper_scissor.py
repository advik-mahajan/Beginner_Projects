import random
while True:
    computer_choice = random.choice(("rock", "paper", "scissor"))
    while True:
        user_choice = input("Enter Your Move: ").lower().strip()
        if user_choice not in ("rock", "paper", "scissor"):
            print("Enter a Valid Choice (rock, paper or scissor)")
            continue
        break
    print(f"You Chose - {user_choice}")
    print(f"Computer Chose - {computer_choice}")
    if user_choice == computer_choice:
        print("Its a Tie")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
    elif user_choice == "scissor" and computer_choice == "paper":
        print("You Win!")
    elif user_choice == "rock" and computer_choice == "scissor":
        print("You Win!")
    else:
        print("You Lose!")
    question = input("Do You Want to Play Again? (yes/no): ").lower().strip()
    if question != "yes":
        break

