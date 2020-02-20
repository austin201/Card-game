import random
class Card(object):
    """ A playing card. This class builds all the cards
    giving them a rank and a suit and can be flipped up or down."""
    RANKS = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    SUITS = ("♠","♥","♣","♦")

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = str.format("""
        -------
        |{0:2}   |
        |{1}    |
        |    {1}|
        |   {0:2}|
        -------
        """,self.rank,self.suit)

        else:
            rep = """
        -------
        |XXXXX|
        |XXXXX|
        |XXXXX|
        |XXXXX|
        -------
        """
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """ A hand of playing cards. This class holds a list of cards for the player. """
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+ ""
        else:
            rep = "Empty"
        return rep
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, other_hand, card):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ A deck of playing cards. This class has the following methods
    def populate build the deck of cards with standard 52 card playing cards.
    def shuffle gathers all the cards and shuffles them up.
    def deal gives the players that are playing the game when started cards."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        import time
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(hand, top_card)
                else:
                    print("Can't continue to deal. A cheater.")
                    time.sleep(3)
                    print("Just kidding I am just out of cards. :)")

if __name__ == "__main__":
    print("This is a module with classes for playing cards")
    input("\n\nPress the enter key to exit.")


# deck = Posdeck()
# deck.populate()
# deck.shuffle()
# hands = []
#
# for i in range(3):
#     hand = Hand()
#     hands.append(hand)
# deck.deal(hands, 3)
# i = 1
# for hand in hands:
#     print("Hand", i)
#     print(hand)
#     i+=1
#
# hands[0].cards[0].flip()
# print(hands[0])
# hands[0].cards[0].flip()
# print(hands[0])

# deck = Deck()
# deck.populate()
# deck.shuffle()
#
# hands = []
# for i in range(3):
#     hand = Hand()
#     hands.append(hand)
# deck.deal(hands, 5)
# i = 1
# for hand in hands:
#     print("Hand ",i)
#     print(hand)
#     i+=1