import random

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
    return random.randint(100, 999)

def input_guesses(code_number):
    """Prompt user to give their answer"""
    code = code_number
    guesses = 10
    
    while guesses > 0:
        guess = input("Please enter a 3 digit number: ")
        guesses -= 1
        
        if win_check(guess, code):
            break
        
        clues = match_check(guess, code)
        print_clues(random.shuffle(clues))
        print(f"You have {guesses} left.")

def convert_to_int_array(string):
    """Break number string into array of single integers"""
    number_array = [int(number) for number in string]
    
    return number_array

def match_check(guess, code_number):
    """Check for exact matches between two arrays"""
    int_guess = convert_to_int_array(guess)
    int_code = convert_to_int_array(str(code_number))
    clues = []
    for i in range(len(int_guess)):
        if int_guess[i] == int_code[i]:
            clues.append("Fermi")
        elif int_guess[i] in int_code:
            clues.append("Pico")
    
    if len(clues) == 0: 
        clues.append("Bagels")

    return clues

def print_clues(clues):
    """Print the clues out to the user"""
    for clue in clues:
        print(clue)

def win_check(guess, code_number):
    """Check if guess matches the code"""
    if int(guess) == code_number:
        print("Congratulations!  You win.")
        return True

def game_loop():
    """Play the game."""
    games_rules()
    code_number = generate_code()
    print(f"The code is {code_number}")
    input_guesses(code_number)

game_loop()