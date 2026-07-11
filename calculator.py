import math
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    if y == 0:
        return "Undefined"
    return x / y
def exp(x, y):
    return x ** y
def sqrt():
    def get_positive():
        while True:
            try:
                num = float(input("Enter the number whose square root you want to find: "))
                if num >= 0:
                    return num
            except ValueError:
                print("Enter a number greater than or equal to zero. ")
    def square_root(x):
        return (x ** 0.5)
    x = get_positive()
    y = square_root(x)
    return y 
def fact():
    def get_positive():
        while True:
            try:
                num = int(input("Enter the number whose factorial you want to find: "))
                if num >=0:
                    return num
            except ValueError:
                print("Invalid input. Enter an integer greater than or equal to 0.")
    def factorial(x):
        return math.factorial(x)
    x = get_positive()
    y = factorial(x)
    return y 
def rem(x, y):
    return (x%y)
def perc(x, y):
    return ((x/y)*100)
def avg():
    def get_qty():
        while True:
            try:
                qty = int(input("How many values do you want to find the average of? -  "))
                if qty >= 2:
                    return qty
            except ValueError:
                print("Enter a number greater than or equal to 2.")
    def average(x):
        total = float(input("Enter the first number: "))
        for i in range(x - 1):
            num = float(input("Enter the next number: "))
            total = total + num
        return total 
    x = get_qty()
    y = average(x)
    return (y/x)
def max():
    def get_qty():
        while True:
            try:
                qty = int(input("Enter the number of values you want to compare: "))
                if qty >= 2:
                    return qty
            except ValueError:
                print("Enter a number greater than or equal to 2.")

    def maximum(x):
        largest = float(input("Enter the first number: "))
        for i in range(x - 1):
            num = float(input("Enter the next number: "))
            if num > largest:
                largest = num
        return largest

    x = get_qty()
    return maximum(x)
def min():
    def get_qty():
        while True:
            try:
                qty = int(input("Enter the number of values you want to compare: "))
                if qty >= 2:
                    return qty
            except ValueError:
                print("Enter a number greater than or equal to 2.")
    def minimum(y):
        smallest = float(input("Enter the first number: "))
        for i in range(y - 1):
            num = float(input("Enter the next number: "))
            if num < smallest:
                smallest = num
        return smallest
    y = get_qty()
    return minimum(y)
def main():
    while True:
        print ("==============================")
        print("          CALCULATOR          ")
        print("==============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Modulus")
        print("9. Percentage")
        print("10. Average")
        print("11. Maximum")
        print("12. Minimum")
        print("13. Exit")
        while True:
            try:
                op = int(input("What mathematical operation would you want to perform? "))
                if 1 <= op <= 13:
                    break
                else:
                    print("Enter a number between 1 and 13.")
            except ValueError:
                print("Enter a number between 1 and 13.")
        if op == 1:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number:"))
            ans = add(x, y)
            print(ans)
        elif op == 2:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            ans = sub(x, y)
            print(ans)
        elif op == 3:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            ans = mult(x, y)
            print(ans)
        elif op == 4:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            ans = div(x, y)
            print(ans)
        elif op == 5:
            x = float(input("Enter the base number: "))
            y = float(input("Enter the exponent: "))
            ans = exp(x, y)
            print(ans)
        elif op == 6:
            ans = sqrt()
            print(f"The square root of the given number is {ans}")
        elif op == 7:
            ans = fact()
            print(f"The factorial of the given number is - {ans}")
        elif op == 8:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            ans = rem(x, y)
            print(f"The remainder is {ans}")
        elif op == 9:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            ans = perc(x, y)
            print(f"{x} is {ans} percent of {y}")
        elif op == 10:
            ans = avg() 
            print (f"The average of the entered numbers is {ans}.")
        elif op == 11:
            ans = max()
            print(f"The largest number is {ans}.")
        elif op == 12:
            ans = min()
            print(f"The smallest number is {ans}.")
        elif op == 13:
            print("Thank You for using my calculator!!")
            break
main()