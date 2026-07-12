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
