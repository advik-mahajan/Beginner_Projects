import random
def get_level():
    print("LEVELS MENU:")
    print("1. Easy - 5 Letter-Word")
    print("2. Medium - 6 Letter-Word")
    print("3. Hard - 7 Letter-Word")
    while True:
        try: 
            level = int(input("Enter the Level Number (1, 2 or 3): "))
            if level in (1, 2, 3):
                break
            else:
                print("Enter a Number between 1 and 3")
                continue
        except ValueError:
            print("Invalid Input")
    return level
def select_word(level):
    easy_words = ("shelf", "snuck", "speed", "squid", "witch", "beach", "hotel", "drive", "frame", "strip",
            "drape", "plain", "crane", "crime", "brick", "bland", "motel", "stink", "track", "trace",
            "cable", "horse", "truck", "train", "moped", "biker", "hiker", "globe", "trunk", "dream")
    medium_words = ("siphon", "serene", "lounge", "laptop", "mobile", "police", "sliver", "artist", "canvas", "clover",
                    "sticky", "runway", "forest", "planet", "suffer", "meadow", "cactus", "friend", "bright", "salmon",
                    "market", "danger", "fabric", "rustic", "ticket", "garden", "silver", "jungle", "rabbit", "random")
    hard_words = ("enfield", "airport", "lantern", "dolphin", "plastic", "captain", "picture", "harvest", "compass", "orchard",
                  "battery", "journey", "freedom", "station", "teacher", "history", "morning", "gallery", "diamond", "chapter",
                  "partner", "fashion", "storage", "federal", "college", "burrito", "plotter", "printer", "batsman", "control")
    match level:
        case 1:
            word_chosen = random.choice(easy_words)
        case 2:
            word_chosen = random.choice(medium_words)
        case 3:
            word_chosen = random.choice(hard_words)
    return word_chosen

def get_letter():
    alphabets = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    while True:
        user_letter = input("Enter Your Guess: ").lower().strip()
        if user_letter not in alphabets:
            print("Enter a Valid Alphabet")
            continue
        else:
            break
    return user_letter

def check_letter(user_letter, word, revealed_letters):
    if user_letter in word:
        for i in range(len(word)):
            if user_letter == word[i]:
                revealed_letters[i] = user_letter
        return True
    else:
        return False

def hangman():
    level = get_level()
    word = select_word(level)
    revealed_letters = ["_"]*len(word)
    wrong_guesses = 0
    guesses_left = 5
    while "_" in revealed_letters and wrong_guesses < 5:
        user_letter = get_letter()
        if check_letter(user_letter, word, revealed_letters) is True:
            pass
        else:
            wrong_guesses += 1
            guesses_left -= 1
            print(f"You Have {guesses_left} Guesses Left!")
        for i in range(len(revealed_letters)):
            print(revealed_letters[i], end=" ")
        print()
    if wrong_guesses == 5:
        print("You Lost! Nice Try!")
        print(f"The Word was: {word}")
    else:
        print("Congratulations! You Won!")

def main():
    hangman()
    while True:
        choice = input("Do You Want to Play Again?(yes or no): ").lower().strip()
        if choice in ("yes", "no"):
            if choice == "yes":
                hangman()
            else:
                break
        else:
            print("Enter either Yes or No")
            continue
main()
