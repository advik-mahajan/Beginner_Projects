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
def sqrt(x):
    return x ** 0.5 
def fact(x):
    return math.factorial(x)
def rem(x, y):
    return (x%y)
def perc(x, y):
    return ((x/y)*100)
def avg(x, y):
     return ((x+y)/2)
def max():
    def get_number():
        while True:
            try:
                qty = int(input("Enter the number of values you want to compare: "))
                if qty >= 2:
                    return qty
            except ValueError:
                print("Enter a number greater than 2.")

    def maximum(x):
        largest = float(input("Enter the first number: "))
        for i in range(x - 1):
            num = float(input("Enter the next number: "))
            if num > largest:
                largest = num
        return largest

    x = get_number()
    return maximum(x)
def min():
    def get_number():
        while True:
            try:
                qty = int(input("Enter the number of values you want to compare: "))
                if qty >= 2:
                    return qty
            except ValueError:
                print("Enter a number greater than 2.")
    def minimum(y):
        smallest = float(input("Enter the first number: "))
        for i in range(y - 1):
            num = float(input("Enter the next number: "))
            if num < smallest:
                smallest = num
        return smallest
    y = get_number()
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
            answer = add(x, y)
            print(answer)
        elif op == 2:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            answer = sub(x, y)
            print(answer)
        elif op == 3:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            answer = mult(x, y)
            print(answer)
        elif op == 4:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            answer = div(x, y)
            print(answer)
        elif op == 5:
            x = float(input("Enter the base number: "))
            y = float(input("Enter the exponent: "))
            answer = exp(x, y)
            print(answer)
        elif op == 6:
            x = float(input("Enter the number: "))
            answer = sqrt(x)
            print(answer)
        elif op == 7:
            x = int(input("Enter the number: "))
            answer = fact(x)
            print(answer)
        elif op == 8:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            answer = rem(x, y)
            print(f"The remainder is {answer}")
        elif op == 9:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            answer = perc(x, y)
            print(f"{x} is {answer} percent of {y}")
        elif op == 10:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            answer = avg(x, y)
            print(f"The average of {x} and {y} is {answer}")
        elif op == 11:
            answer = max()
            print(f"The largest number is {answer}.")
        elif op == 12:
            answer = min()
            print(f"The smallest number is {answer}.")
        elif op == 13:
            print("Thank You for using my calculator!!")
            break
main()