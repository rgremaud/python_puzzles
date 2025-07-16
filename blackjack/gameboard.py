from deck import Deck
from players import Player
from players import Human
from players import Dealer
from rules import Rules

import random

class Gameboard:
    """A class to build the blackjack gameboard"""

    def __init__(self):
        """Initialize a game of blackjack"""
        self.deck = Deck()
        self.rules = Rules()
        self.human = Human(deck=self.deck)
        self.dealer = Dealer(deck=self.deck)
        self.initial_hit = True
        
    
    def build_game(self):
        """Run the game loop the game"""
        self.get_wager()
        self.deal_a_hand()
        self.print_hand(self.deck.human_hand)
        self.print_dealer_hand(self.deck.dealer_hand)
        

    def stand_check(self):
        """Direct the flow of a hand"""
        if self.human.stand == False and self.dealer.stand == False:
            self.hit_stand_doubledown()
            self.dealer_move()
        elif self.human.stand == True and self.dealer.stand == False:
            self.dealer_move()
        elif self.human.stand == False and self.dealer.stand == True:
            self.hit_stand_doubledown()
        
    
    def hit_stand_doubledown(self):
        """Prompt human to hit stand or double down"""
        print("Would you like to hit, stand or double down?")
        print("Double down is only available on your first turn,")
        print("and you will hit exactly one more time before standing.")
        if self.initial_hit == True:
            move = input("Please enter H, S or DD: ")
            self.initial_hit = False
        else:
            move = input("Please enter H, S: ")

        if move == "H":
            self.hit(self.human.hand)
        elif move == "S":
            self.stand(self.human.hand)
        elif move == "DD":
            self.doubledown()
        
        self.stand_check()
    
    def dealer_move(self):
        """Calculate the dealer moves"""
        self.dealer.count = self.calculate_count(self.dealer.hand)
        if self.dealer.count <= 16:
            self.hit(self.dealer.hand)
        elif self.dealer.count >= 17:
            self.stand(self.dealer.hand)
    
    def hit(self,hand):
        """Deal an additional card to the human and then prompt for hit, stand."""
        card = self.deal_a_card()
        hand.append(card)
        self.dealer_move()
        self.bust_check(hand)

        self.stand_check()

    def bust_check(self, hand):
        """Check if hand has busted"""
        count = self.calculate_count(hand)

        if count > self.rules.max_count and hand == self.human.hand:
            print(f"You have busted!  With a score of {count}")
            self.human.money -= int(self.current_wager)
            self.another_round()
        elif count > self.rules.max_count and hand == self.dealer.hand:
            self.print_hand(self.human.hand)
            self.print_hand(self.dealer.hand)
            print("Dealer has busted.  You win!")
            self.human.money += int(self.current_wager)
            self.another_round()

    
    def stand(self, hand):
        """Calculate final totals and show score"""
        if hand == self.human.hand:
            self.human.stand = True

        if hand == self.dealer.hand:
            self.dealer.stand = True
    
    def doubledown(self):
        """Double wager, deal one more card to human and calculate final totals"""
        self.human.wager *= 2
        card = self.deal_a_card()
        human_count = self.calculate_count(self.human.hand)
        dealer_count = self.calculate_count(self.dealer.hand)
        return self.final_count(human_count, dealer_count)
    
    def final_count(self, human_count, dealer_count):
        """Calculate the final total and declare winner"""
        if human_count > dealer_count:
            self.human.money += self.human.wager
            print(f"You win! Human count: {self.human.count}, Dealer count: {self.dealer.count}")
            print(f"You now have ${self.human.money}")
        elif human_count < dealer_count:
            self.human.money -= self.human.wager
            print(f"You lose! Human count: {self.human.count}, Dealer count: {self.dealer.count}")
            print(f"You now have {self.human.money}")
        else:
            print(f"Its a tie! Human count: {self.human.count}, Dealer count: {self.dealer.count}")
        
        self.another_round()
    
    def another_round(self):
        """Ask user if they want to play another round"""
        answer = input("Player another round? Enter Y or N: ")
        if answer == "Y":
            self.deck = Deck()
            self.human.hand = []
            self.dealer.hand = []
            self.human.stand = False
            self.dealer.stand = False
            self.initial_hit = True
            self.game_loop()
        else:
            print(f"Cya next time!  You finished with {self.human.wager} dollar bucks")
            return

    def calculate_count(self,hand):
        """Calculate the count of a hand"""
        count = 0
        number_of_aces = 0
        i = 0 
        
        for card in hand:
            if card[1] == "A":
                number_of_aces += 1
            elif card[1] == "J": 
                count += 10
            elif card[1] == "Q":
                count += 10
            elif card[1] == "K":
                count += 10
            else:
                count += card[1]
        
        while i < number_of_aces:
            if count + 11 <= self.rules.max_count:
                count += 11
            else:
                count += 1
            i += 1
       
        return count
                
    def get_wager(self):
        """Ask the human how much they want to wager"""
        print(f"Money: {self.human.money}")
        self.current_wager = input(f"How much would you like to wager: (1-{self.human.money}) or quit ")
        while True:
            if self.current_wager == 'quit':
                False
                break
            else:
                self.human.wager += int(self.current_wager)
                return
    
    def deal_a_hand(self):
        """Deal a hand to the human and dealer"""
        card_1, card_2 = self.deal_a_card(), self.deal_a_card()
        card_3, card_4 = self.deal_a_card(), self.deal_a_card()
        self.deck.human_hand.append(card_1)
        self.deck.human_hand.append(card_2)
        self.deck.dealer_hand.append(card_3)
        self.deck.dealer_hand.append(card_4)
    
    def deal_a_card(self):
        """Deal a card from the deck """
        random_suit = random.choice(list(self.deck.cards.keys()))
        random_card = random.choice(self.deck.cards[random_suit])
        card = [random_suit, random_card]
        card_index = self.deck.cards[random_suit].index(random_card)
        del self.deck.cards[random_suit][card_index]
        return card
    
    def remove_card(self, card):
        """Remove card from deck"""
        self.deck.cards[card[0]].remove(card[1])

    def show_card(self, card): 
        """Draw cards"""
        print(" ___")
        print(f"|{card[1]}  |")
        print(f"| {card[0]} |")
        print(f"|__{card[1]}|")
    
    def print_dealer_hand(self, dealer_hand): 
        """Print dealer hand with first card hidden"""
        dealer_line_1, dealer_line_2, dealer_line_3, dealer_line_4 = "", "", "", ""
        for card in dealer_hand:
            if card == dealer_hand[0]: 
                dealer_line_1 += (" ___     ")
                dealer_line_2 += ("|#  |    ")
                dealer_line_3 += ("| # |    ")
                dealer_line_4 += ("|__#|    ")
            else:
                dealer_line_1 += (" ___     ")
                dealer_line_2 += (f"|{card[1]}  |    ")
                dealer_line_3 += (f"| {card[0]} |    ")
                dealer_line_4 += (f"|__{card[1]}|    ")
        
        print(dealer_line_1)
        print(dealer_line_2)
        print(dealer_line_3)
        print(dealer_line_4)
        
    def print_hand(self, human_hand):
        human_line_1, human_line_2, human_line_3, human_line_4 = "", "", "", ""
        
        for card in human_hand:
            human_line_1 += (" ___     ")
            human_line_2 += (f"|{card[1]}  |    ")
            human_line_3 += (f"| {card[0]} |    ")
            human_line_4 += (f"|__{card[1]}|    ")

        print(human_line_1)
        print(human_line_2)
        print(human_line_3)
        print(human_line_4)


blackjack = Gameboard()
blackjack.rules.intro_rules()
blackjack.build_game()