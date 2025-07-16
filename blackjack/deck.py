class Deck:
    """A class to represent a deck of cards"""
    
    def __init__(self):
        """Initialize the deck of cards"""
        self.cards = {"♣": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
                "♦": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
                "♥": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
                "♠": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]}
        
        self.human_hand = []
        self.dealer_hand = []