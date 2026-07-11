'''
need to make a code where the user enters as many integers are he or she wants to. 
the number of numbers has to be greater than 2 to compare
then return the largest number
'''
def get_number():
    while True:
        try:
            qty = int(input("Enter the number of inputs you want to compare: "))
            if qty >= 2:
                break
            else:
                continue
        except ValueError:
            print("The number of inputs have to be greater than 2.")
    return qty
x = get_number()
def get_max():
    number1 = float(input("Enter a number: "))
    largest = number1
    for i in range(x - 1):
        num = float(input("Enter a number: "))
        if num > largest:
            largest = num
    return largest
ans = get_max()
print(f"The largest number is: {ans}")    


    
