SLOTS - CLI Slot Machine Game

A simple terminal-based slot machine game built in Python

HOW TO PLAY:

1) Run the script
2) Read the menu to see the symbols, their probabilities and rewards
3) Enter a bet amount (has to be greater than zero and less than or equal to your balance)
4) Three symbols are randomly rolled
5) If all three match, you win based on the symbol
6) If all three symbols dont match, you lose the bet
7) Choose to play again or quit after each round
8) Game ends if your balance hits $0 

SYMBOLS AND PAYOUTS:

1) Bomb - 3% chance - entire balance hits zero, no matter the bet amount
2) Number 7 - 7% chance - entire balance gets multiplied by 7, no matter the bet amount
3) Diamond - 15% chance - 50% of the bet amount
4) Cherry - 20% chance - 25% of the bet amount
5) Stars - 25% chance - 10% of the bet amount

FEATURES:

1) Weighted random symbol generation using random.choices()
2) Input validation for bet amount (handles invalid / out of range amounts)
3) Play-again loop with validation
4) Game over if the balance reaches zero

TECHNOLOGIES USED:

1) Python 3.x
2) Built-in random module
