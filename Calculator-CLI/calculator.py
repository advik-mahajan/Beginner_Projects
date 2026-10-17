import math
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def get_qty():
    while True:
        try:
            qty = int(input("How many numbers do you want to evaluate? "))
            if qty > 0:
                break
            else:
                print("Enter a number greater than zero.")
                continue
        except ValueError:
            print("Enter a valid quantity.")
    return qty
def addition():
    x = get_qty()
    sum = 0
    for _ in range (x):
        num = float(input("Enter a number: "))
        sum = sum + num
    return sum 
def subtraction():
    x = get_qty()
    diff = float(input("Enter the first number: "))
    for _ in range (x-1):
        num = float(input("Enter a number: "))
        diff = diff - num
    return diff 
def product():
    x = get_qty()
    product = 1
    for _ in range (x):
        num = float(input("Enter a number: "))
        product = product * num
    return product 
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
    if y == 0:
        return "Undefined"
    else:
        return((x/y)*100)
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
    def minimum(y):
        smallest = float(input("Enter the first number: "))
        for i in range(y - 1):
            num = float(input("Enter the next number: "))
            if num < smallest:
                smallest = num
        return smallest
    y = get_qty()
    return minimum(y)
def quadratic():
    print("Please arrange your equation in the format - ax^2 + bx + c = 0 ")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    det = b**2 - (4*a*c)
    if det < 0:
        print("The roots of the given equation are imaginary.")
    else:
        sum_of_roots = (-b / (2*a))
        product_of_roots = (c / a)
        root1 = (-b + math.sqrt(det)) / (2*a)
        root2 = (-b - math.sqrt(det)) / (2*a)
        if det == 0:
            print("The roots are real and equal.")
        else:
            print("The roots are real.")
        print(f"The value of roots are: {root1} and {root2}.")
        print(f"Sum of roots is {sum_of_roots}.")
        print(f"Product of roots is {product_of_roots}.")
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
        print("13. Quadratic Equation Solver")
        print("14. Exit")
        while True:
            try:
                op = int(input("What mathematical operation would you want to perform? "))
                if 1 <= op <= 14:
                    break
                else:
                    print("Enter a number between 1 and 14.")
            except ValueError:
                print("Enter a number between 1 and 14.")
        if op == 1:
            sum = addition()
            print(f"Sum of the given numbers is {sum}.")
        elif op == 2:
            diff = subtraction()
            print(f"Difference of the given numbers is {diff}.")
        elif op == 3:
           prod = product()
           print(f"Product of the given numbers is {prod}.")
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
            quadratic()
        elif op == 14:
            print("Thank You for using my calculator!!")
            break
main()
