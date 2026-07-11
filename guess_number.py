#guessing number game
import random
number = random.randint(1, 100)
total = 1
while True:
    while True:
        try:
            guess = int(input("Enter a number: "))
            if 1 <= guess <=100:
              break  
            else:
                print("Enter a number between 1 and 100. ")
                
        except ValueError:
            print("Enter a number between 1 and 100.")        
    if guess == number:
        print("Congratulations!, you guessed it right. ")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
    total = total + 1
print(f"You guessed in {total} attempts.")
print("Thank you for playing the game!")





