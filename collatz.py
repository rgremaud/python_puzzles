# The Collatz sequence, also called the 3n + 1 problem,
# is the simplest impossible math problem. (But don’t worry,
# the program itself is easy enough for beginners.)
# From a starting number, n, follow three rules to get the next number in the sequence:

# If n is even, the next number n is n / 2.
# If n is odd, the next number n is n * 3 + 1.
# If n is 1, stop. Otherwise, repeat.
# It is generally thought, but so far not mathematically proven,
# that every starting number eventually terminates at 1.
# More information about the Collatz sequence can be found at https://en.wikipedia.org/wiki/Collatz_conjecture.


def collatz(number):
    """Run the Collatz conjecture until you get to 1"""
    number_list = []
    while number != 1:
        if number % 2 == 0:
            number_list.append(int(number))
            number /= 2
        elif number % 2 != 0:
            number_list.append(int(number))
            number = number * 3 + 1
    number_list.append(1)
    print(number_list)


collatz(26)
