import random
balance = 100

def menu():
    print("Welcome to Slots!")
    print("Symbols - 🍒 💎 7️⃣ ⭐ 💣")
    print("SYMBOLS GUIDE:")
    print("1. Bomb 💣💣💣 - 3% chance - Lose Entire Balance")
    print("2. Seven 7️⃣ 7️⃣ 7️⃣ - 7% chance - Balance Multiplied by 7 ")
    print("3. Diamond 💎💎💎 - 15% chance - 50% of Bet Amount")
    print("4. Cherry 🍒🍒🍒 - 20% chance - 25% of Bet Amount")
    print("5. Star ⭐⭐⭐ - 25% chance - 10% of Bet Amount")
    print("Your Starting Balance is $100")

def get_bet_amount():
    while True:
        try:
            bet = int(input("Enter Bet Amount: "))
            if bet <= 0:
                print("Enter an Amount Greater than Zero")
            elif bet > balance:
                print("Insufficient Balance. Try Again.")
            else:
                return bet
        except ValueError:
            print("Enter a Valid Amount")

def slot_generator(bet):
    global balance
    symbols = ["💣", "7️⃣", "💎", "🍒", "⭐"]
    weights = [3, 7, 15, 20, 25]
    slot1 = random.choices(symbols, weights=weights, k=1)[0]
    slot2 = random.choices(symbols, weights=weights, k=1)[0]
    slot3 = random.choices(symbols, weights=weights, k=1)[0]
    print(f"Your Slot - {slot1} {slot2} {slot3}")

    if slot1 == slot2 == slot3:
        winning_symbol = slot1
        payouts = {"💣": "wipe",
                   "7️⃣": 7,
                   "💎": 0.50,
                   "🍒": 0.25,
                   "⭐": 0.10}
        if winning_symbol == "💣":
            balance = 0
        elif winning_symbol == "7️⃣":
            balance = balance * 7
        else:
            balance = balance + (bet * payouts[winning_symbol])
    else:
        print("No Matches. You Lost your Bet!")
        balance = balance - bet

    print(f"Your Updated Balance is: ${balance}\n")

def main():
    menu()
    while True:
        if balance <= 0:
            print("You're out of balance! Game Over.")
            break
        bet = get_bet_amount()
        slot_generator(bet)
        while True:
            choice = input("Do You Want to Play Again?: ").lower().strip()
            if choice in ("yes", "no"):
                break
            else:
                print("Enter either Yes or No")
                continue
        if choice == "yes":
            continue
        else:
            break

main()
