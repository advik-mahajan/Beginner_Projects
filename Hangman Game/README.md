HANGMAN CLI:
A terminal-based Hangman game built in Python, with three difficulty levels based on word length.

FEATURES:

1) Three difficulty levels with 30 words each
2) Input validation (rejects non-alphabet input, handles case/whitespace)
3) Live-updating display of guessed progress after every turn
4) Tracks remaining wrong guesses
5) Clear win/loss messaging at the end of the game

PROJECT STRUCTURE:

1) get_level() - prompts the player to choose a difficulty
2) select_word(level) - picks a random word from the matching word bank
3) get_letter() - validates and returns a single letter guess
4) check_letter(user_letter, word, revealed_letters) - checks the guess against the word and updates the revelead letters list in place
5) hangman() - main game loop tying everything together

TECHNOLOGIES USED:

1) Python 3
2) Built-in random module

REQUIREMENTS:

1) Python 3.x
