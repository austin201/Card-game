import Card as C
import game as G

class BJ_Card(C.Card):
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank)+1
            # if card is a face card
            if v > 10:
                v = 10
        else:
            v = None
        return v
class BJ_Deck(C.Deck):
    """A Black Jack Deck."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(C.Hand):
    """A Black Jack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        # if a card in the hand has value of None, then total is None.
        for card in self.cards:
            if not card.value:
                return None
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value
        #determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            #add only 10 since we've already added 1 for the Ace
            t += 10
        return t
    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = G.ask_yes_no("\n" + self.name + ", do you want to hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses")

    def win(self):
        print(self.name, "wins")

    def push(self):
        print(self.name, "pushes")

class BJ_Dealer(BJ_Player):
    def is_hitting(self):
        return self.total < 17

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """ A Black Jack Game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
    def play(self):
        # deal intial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand= 2)
        self.dealer.flip_first_card()# hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)
        # reveal dealer's first card
        self.dealer.flip_first_card()

        if not self.still_playing:
            #since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing():
                    player.win()
            else:
                for player in self.still_playing():
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tWelcome to Black Jack>\n")
    names = []
    number = G.ask_number("How many players? (1-7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = G.ask_yes_no("\nDo you want to play again?: ")

main()
