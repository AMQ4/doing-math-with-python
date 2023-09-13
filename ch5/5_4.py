"""
#4: Shuffling a Deck of Cards

Consider a standard deck of 52 playing cards. Your challenge here is to
write a program to simulate the shuffling of this deck. To keep the imple-
mentation simple, I suggest you use the integers 1, 2, 3, . . . , 52 to represent
the deck. Every time you run the program, it should output a shuffled
deck—in this case, a shuffled list of integers.
"""

from random import shuffle

class Card:
    """
    Represents a playing card with a suit and rank.
    """
    def __init__(self, suit, rank):
        """
        Initializes a new Card object with the specified suit and rank.

        Args:
            suit (str): The suit of the card (e.g., "Spades (♠)").
            rank (str or int): The rank of the card (e.g., "Ace" or an integer).
        """
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        """
        Returns a string representation of the card.

        Returns:
            str: A string in the format "{rank} of {suit}".
        """
        return f"{self.rank} of {self.suit}"
    

suits = ["Spades (♠)", "Hearts (♥)", "Diamonds (♦)", "Clubs (♣)"]
cards = ["Ace", "Jack", "Queen", "King", 2, 3, 4, 5, 6, 7, 8, 9, 10]

deck = [Card(suit, rank) for suit in suits for rank in cards]
shuffle(deck)
print(deck)
