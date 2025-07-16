class Rules:
    """Generate the rules for blackjack"""

    def __init__(self):
        """Initialize rules for blackjack"""
        self.max_count = 21

    def intro_rules(self):
        """Print intro rules for game."""
        print("Rules:\n")
        print("\tTry to get as close to 21 without going over.")
        print("\tKings, Queens, and Jacks are worth 10 points.")
        print("\tAces are worth 1 or 11 points.")
        print("\tCards 2 through 10 are worth their face value.")
        print("\t(H)it to take another card.")
        print("\t(S)tand to stop taking cards.")
        print("\tOn your first play, you can (D)ouble down to increase your bet")
        print("\tbut must hit exactly one more time before standing.")
        print("\tIn case of a tie, the bet is returned to the player.")
        print("\tThe dealer stops hitting at 17.")
        print(f"\n")

    