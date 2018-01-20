import random
from poker_hand import PokerHand
from poker_judger import PokerJudger


class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        return "{}{}".format(self.val, self.suit)


class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["s", "c", "d", "h"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        lst = []
        for card in self.hand:
            lst.append(card.show())
        print(lst)

##############################################################################

# deck = Deck()
# deck.shuffle()
# deck.show()
#
# foo = Player("foo")
# foo.draw(deck).draw(deck).draw(deck)
# foo.showHand()
#
# players = [Player("player{}".format(i)) for i in range(0, 10)]
# ret = []
# for player in players:
#     player.draw(deck).draw(deck).draw(deck)
#     ret.append(" ".join(player.showHand()))
#
# print(ret, PokerJudger.get_winner(ret))
