
# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. 
# The game offers one of the following hints in response to your guess: “Pico” when your guess 
# has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the 
# correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.

import random

# Lay out rules of the game via print

code_number = ""
code_list = ""

def game_loop():
    """Play the game."""
    games_rules()
    generate_code()
    input_guesses()


def games_rules():
    """Layout the rules of the game."""
    print("I am thinking of a 3 digit number")
    print("You will have 10 chances to guess the number")
    print('You will be given a response of "Pico" for a correct digit, in the wrong place')
    print('You will be given a response of "Fermi" for a correct digit in the correct place')
    print('You will be given a response of "Bagels" for no correct digits.')
    print("You have 10 tries to guess.  Good luck!")

def generate_code():
    """Randomly generate the code number between 100-999"""
    code_number = random.randint(100, 999)
    print(f"The code is {code_number}")
    code_list = list(str(code_number))
    print(code_list)

def input_guesses():
    """Prompt user to give their answer"""
    guesses = 10
    guess = ""
    # build a loop that runs while number of guesses remains > 0 or guess != answer
    while guesses > 0:
        guess = input("Please enter a 3 digit number: ")
        guesses -= 1
        guess_list = list(str(guess))
        win_check(guess_list)
        print(f"You have {guesses} left.")

def win_check(guess):
    """Check if guess matches the code"""
    print(f"Your guess is {guess} an the code is {code_number}")
    if guess == code_list:
        print("Congratulations!  You win.")

game_loop()