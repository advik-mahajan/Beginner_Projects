def get_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            if 0 < number <= 20:
                break
            else:
                continue
        except ValueError:
            print("Enter an integer between 1 and 20.")
    return number
n = get_number()
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
        
    for j in range(i+1):
        print("#", end="")
    print()

