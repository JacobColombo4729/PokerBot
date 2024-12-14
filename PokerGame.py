import random

class Card:
    """
    A class representing a single playing card in Poker.
    """
    RANKS = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': [1, 14]  # Ace can be either 1 or 14
    }
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self, rank, suit, ace_high=True):
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        
        self.rank = rank
        self.suit = suit
        
        if rank == 'A':
            self.value = Card.RANKS['A'][1] if ace_high else Card.RANKS['A'][0]
        else:
            self.value = Card.RANKS[rank]
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """
    A class representing a deck of cards for a Texas Hold'em card game.
    """
    def __init__(self, ace_high=True):
        self.cards = []
        self.ace_high = ace_high
        self.reset_deck()

    def reset_deck(self):
        """
        Resets the deck to the full 52 cards (without jokers).
        """
        self.cards = [Card(rank, suit, self.ace_high) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle_deck()
        
    def shuffle_deck(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)
        
    def draw_card(self):
        """
        Draws the top card from the deck.
        :return: The top card of the deck, or None if the deck is empty.
        """
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def deal_hand(self, num_players):
        """
        Deals two cards to each player for Texas Hold'em.
        :param num_players: Number of players to deal hands to.
        :return: A list of lists, where each inner list contains two cards for a player.
        """
        hands = []
        for _ in range(num_players):
            hand = [self.draw_card(), self.draw_card()]
            hands.append(hand)
        return hands

    def deal_flop(self):
        """
        Deals the flop (3 community cards).
        :return: A list of 3 cards (the flop).
        """
        flop = [self.draw_card(), self.draw_card(), self.draw_card()]
        return flop
    
    def deal_turn(self):
        """
        Deals the turn (the 4th community card).
        :return: The 4th card (the turn).
        """
        return self.draw_card()

    def deal_river(self):
        """
        Deals the river (the 5th community card).
        :return: The 5th card (the river).
        """
        return self.draw_card()

    def __repr__(self):
        """
        String representation of the deck (list all the cards).
        """
        return ', '.join([repr(card) for card in self.cards])

# Example Usage
deck = Deck(ace_high=True)  # Ace is treated as 14

# Deal hands for 4 players
hands = deck.deal_hand(4)
print("Hands dealt to players:")
for idx, hand in enumerate(hands):
    print(f"Player {idx + 1}: {hand}")

# Deal the flop (3 community cards)
flop = deck.deal_flop()
print("\nFlop:")
print(flop)

# Deal the turn (4th community card)
turn = deck.deal_turn()
print("\nTurn:")
print(turn)

# Deal the river (5th community card)
river = deck.deal_river()
print("\nRiver:")
print(river)

