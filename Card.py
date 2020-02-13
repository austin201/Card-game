import random
class Card(object):
    RANKS = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    SUITS = ("♠","♥","♣","♦")

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = str.format("""
        -------
        |{0:2}   |
        |{1}    |
        |    {1}|
        |   {0:2}|
        -------
        """,self.rank,self.suit)
        return rep

class Hand(object):
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
                    print("Just kidding I am just out of cards.")

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = False):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
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

class Posdeck(Deck):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Positionable_Card(rank, suit))

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