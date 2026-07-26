import random
def level_select():
    print("Welcome to GuessX - a number guessing game")
    print("LEVEL MENU:")
    print("1. Easy - guess a number between 1 and 50")
    print("2. Medium - guess a number between 1 and 100")
    print("3. Hard - guess a number between 1 and 200")
    print("4. Extreme - guess a number between 1 and 500")
    while True:
        try:
            level = int(input("Enter your Level Choice: "))
            if 1 <= level <= 4:
                break
            else:
                print("Invalid Input. Enter a Number between 1 and 4.")
        except ValueError:
            print("Enter a Number between 1 and 4.")
    return level 
def guessx_game():
    level = level_select()
    if level == 1:
        low = 1
        high = 50
    elif level == 2:
        low = 1
        high = 100
    elif level == 3:
        low = 1
        high = 200
    else:
        low = 1
        high = 500
    random_number = random.randint(low, high)
    guesses = 0
    while True:
        guess = int(input("Enter your Guess: "))
        guesses += 1
        if not (low <= guess <= high):
            print(f"Enter a Number between {low} and {high}")
        elif guess == random_number:
            print("Congratulations! You Guessed Right!")
            print(f"You Guessed in {guesses} Attempts")
            break
        elif guess > random_number:
            print("Too High!")
        else:
            print("Too Low!")
while True:
    guessx_game()
    play_again = input("Do you Want to Play Again? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("Thanks for playing!")
        break
