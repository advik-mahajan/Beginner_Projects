pin = 4444
in_bal = 10000
def authenticate():
    attempts = 3
    while attempts > 0:
        try:
            entered_pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Enter a valid PIN.")
            continue 
        if not (1000 <= entered_pin <= 9999):
            print("Enter a valid 4 digit PIN.")
            continue
        if entered_pin == pin:
            print("Login Successful!\n")
            return True
        else:
            attempts = attempts - 1
            if attempts >  0:
                print(f"Incorrect PIN, you have {attempts} attempt(s) left.")
            else:
                print("Too many incorrect attempts. Account locked. ")
                return False
def withdraw():
    global in_bal
    while True:
        try:
            withdrawal_amount = int(input("Enter the amount you want to withdraw (0 to cancel): "))
            if withdrawal_amount == 0:
                print("Withdrawal cancelled.")
                return
            elif withdrawal_amount < 0: 
                print("Enter a positive amount.")
            elif withdrawal_amount > in_bal:
                print("Insufficient funds.")
            else:
                in_bal = in_bal - withdrawal_amount
                print(f"Withdrawal of {withdrawal_amount} successful!")
                print(f"Updated Balance - {in_bal}")
                break
        except ValueError:
            print("Enter a valid amount")            
def deposit():
    global in_bal
    while True:
        try:
            deposit_amount = int(input("Enter the amount you want to deposit (0 to cancel): "))
            if deposit_amount == 0:
                print("Deposit cancelled.")
            elif deposit_amount < 0:
                print("Enter a positive amount.")    
            else:
                in_bal = in_bal + deposit_amount
                print(f"Successful deposit of {deposit_amount}")
                print(f"Updated Balance - {in_bal}")
                break            
        except ValueError:
            print("Enter a valid amount")
def atm_sim():
    print("Please authenticate your PIN to access the menu.")
    if not authenticate():
        return
    print("Welcome to the ATM Simulator!!")
    print("1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Exit")
    while True:
        try:
            action = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid choice")
            continue
        if action == 1:
            withdraw()
        elif action == 2:
            deposit()
        elif action == 3:
            print("Thank You for using ATM Simulator!")
            break
        else:
            print("Enter a valid choice.")
atm_sim()
