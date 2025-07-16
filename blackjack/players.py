class Player:
    """A class to initiate players for blackjack"""

    def __init__(self,deck):
        """Initialize the players for game"""
        self.deck = deck
        self.count = 0
        self.stand = False

class Dealer(Player):
    """A sub class of player for the computer dealer."""
    
    def __init__(self, deck):
        super().__init__(deck)
        self.hand = self.deck.dealer_hand

class Human(Player):
    """A sub class for human player."""
    def __init__(self, deck):
        super().__init__(deck)
        self.hand = self.deck.human_hand
        self.money = 5_000
        self.wager = 0