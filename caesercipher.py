def caeser_cipher(string, shift):
    """Testing new caeser shift function w/better format"""
    # Set initial variables
    alphabet = build_list("abcdefghijklmnopqrstuvwxyz")
    string_list = build_list(string)
    caeser_list = []

    # run shift
    for letter in string_list:
        if letter in alphabet:
            new_letter = run_shift(letter, alphabet, shift)
            caeser_list.append(new_letter)
        else:
            caeser_list.append(letter)

    shift_string = "".join(caeser_list)
    print(shift_string)


def run_shift(letter, alphabet, shift):
    """Shift letter to new value"""
    initial_number = alphabet.index(letter)
    shift_number = initial_number + shift
    if shift_number >= 0 and shift_number <= 25:
        new_letter = alphabet[shift_number]
    elif shift_number > 25:
        shift_number = shift_number % 26
        new_letter = alphabet[shift_number]
    elif shift_number < 0:
        shift_number = shift_number % 26
        new_letter = alphabet[shift_number]
    return new_letter


def build_list(string):
    """Take string and break it a list"""
    char_list = list(string.lower())
    return char_list


def cipher_prompt():
    """Prompt user to figure out actions"""
    answer = ""
    while answer != "d" or answer != "e":
        answer = str(
            input("Would you like to encrypt or decrypt a message?  Enter e or d. ")
        )
        if answer == "e":
            string = str(input("Please enter string to encrypt: "))
            shift = get_integer_input("Please enter the shift amount: ")
            caeser_cipher(string, shift)
            break
        elif answer == "d":
            string = str(input("Please enter string to decrypt: "))
            shift = (
                int(get_integer_input("Please enter the original shift amount: ")) * -1
            )
            caeser_cipher(string, shift)
            break


def get_integer_input(prompt):
    """Get integer input"""
    while True:
        user_input = input(prompt)
        try:
            integer_value = int(user_input)
            return integer_value  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def caeser_hacker(string):
    """Take a string and loop it for all possible inputs"""
    # take the string and loop it 26 times
    i = 1
    while i <= 26:
        caeser_cipher(string, i)
        i += 1


# cipher_prompt()
caeser_hacker("uryyb, jbeyq!")
