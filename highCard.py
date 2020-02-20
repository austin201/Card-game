import Card
#help(Card)
def get_name():
    name = ""
    while name == "":
        name = input("Enter your player name: ")
    return name

total_players = int(input("How many players are playing High Card: "))
names = []
hands = []
for i in range(total_players):
    x = get_name()
    hand = Card.Hand()
    hands.append(hand)
    names.append(x)
deck = Card.Deck()
deck.populate()
deck.shuffle()
deck.deal(hands, 1)

for hand in hands:
    print(hand)

#This is how Carter did it.
# class highcard(Card.Card):
#     def __init__(self, rank, suit, value):
#         super(highcard, self).__init__((rank, suit))
#         self.value = value
#
# class highcardDeck(Card.Deck):
#     def populate(self):
#         for suit in highcard.SUITS:
#             for rank in highcard.RANKS:
#                 if rank == "A":
#                     value = 14
#                 elif rank == "J":
#                     value = 11
#                 elif rank == "Q":
#                     value = 12
#                 elif rank == "K":
#                     value = 13
#                 else:
#                     value = int(rank)
#                 self.cards.append(highcard(rank, suit, value))

class highcard(Card.Card):
    def __init__(self, rank, suit):
        super(highcard, self).__init__((rank, suit))

    @property
    def value(self):
        if self.is_face_up:
            v = highcard.RANKS.index(self.rank)+1
            if v == 1:
                v +=13
        else:
            v = None
        return v

class highcardDeck(Card.Deck):
    def populate(self):
        for suit in highcard.SUITS:
            for rank in highcard.RANKS:
                self.cards.append(highcard(rank, suit))
class highcardHand(Card.Hand):
    def __init__(self, name):
        super(highcardHand, self).__init__()
        self.name = name
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        return t
    def win(self):
        print(self.name)
        print("Winner")
    def loose(self):
        print(self.name)
        print("Looser")

def get_name():
    name = ""
    while name == "":
        name = input("Enter your name: ")
    return name

total_players = int(input("How many players are playing: "))
hands = []
for i in range(total_players):
    x = get_name()
    hand = highcardHand(x)
    hands.append(hand)

deck = highcardDeck()
deck.populate()
deck.shuffle()
deck.deal(hands, 1)

highcard = 0
for player in hands:
    print(player)
    if player.total > highcard:
        highcard = player.total

for player in hands:
    if player.total >= highcard:
        player.win()
    else:
        player.loose()