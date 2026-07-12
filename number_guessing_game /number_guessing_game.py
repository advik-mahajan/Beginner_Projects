import random 
def get_input():
    while True:
        try:
            guess = int(input("Enter Your Guess: "))
            if 0 <= guess <= 100:
                return guess
            else:
                print("Invalid Input.")
        except ValueError:
            print("Invalid Input.")
def play_game():
    random_number = random.randint(1, 100)
    print("The random number chosen is between 0 and 100, both included.")
    number_of_guesses = 0
    while True:
        x = get_input()
        number_of_guesses += 1
        if x > random_number:
            print("Too High!")
        elif x < random_number:
            print("Too Low!")
        else:
            print("Congratulations!, You Guessed Right!")
            print(f"You guessed in {number_of_guesses} attempts.")
            break
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again != "yes":
        print("Thanks for playing!")
        break
import random
random_number = random.randint(1, 100)
print("The random number chosen is between 0 and 100 (both included). ")
def get_input():
    while True:
        try:
            guess = int(input("Enter Your Guess: "))
            if 0 <= guess <= 100:
                break
            else:
                print("Invalid Input.")
        except ValueError:
            print("Invalid Input.")
    return guess 
number_of_guesses = 0
while True:
    x = get_input()
    number_of_guesses += 1 
    if x > random_number:
        print("Too High!")
    elif x < random_number:
        print("Too Low!")
    elif x == random_number:
        print("Congratulations!, You Guessed Right!")
        print(f"You guessed in {number_of_guesses} attempts.")
        break
