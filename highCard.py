import Card

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
