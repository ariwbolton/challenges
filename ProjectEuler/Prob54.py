

HIGH_CARD       = 1
ONE_PAIR        = 2
TWO_PAIRS       = 3
THREE_OF_KIND   = 4
STRAIGHT        = 5
FLUSH           = 6
FULL_HOUSE      = 7
FOUR_OF_KIND    = 8
STRAIGHT_FLUSH  = 9
ROYAL_FLUSH     = 10

ranks = [
    HIGH_CARD,
    ONE_PAIR,
    TWO_PAIRS,
    THREE_OF_KIND,
    STRAIGHT,
    FLUSH,
    FULL_HOUSE,
    FOUR_OF_KIND,
    STRAIGHT_FLUSH,
    ROYAL_FLUSH
]

PLAYER_1 = 1
PLAYER_2 = 2

def charToNum(c):
    if c == "A":
        return 14
    elif c == "K":
        return 13
    elif c == "Q":
        return 12
    elif c == "J":
        return 11
    elif c == "T":
        return 10
    else:
        return int(c)

def suitToNum(c):
    if c == "H":
        return 1
    elif c == "D":
        return 2
    elif c == "C":
        return 3
    else:
        return 4 

class Rank():
    self __init__(self, rankType, highCards, highSuit)

class Card():
    def __init__(self, cardString):
        self.num, self.suit = charToNum(cardString[0]), suitToNum(cardString[1])
        self.cardString = cardString

    def __gt__(self, c2):
        if self.num == c2.num:
            return self.suit > c2.suit

        return self.num > c2.num

    def __repr__(self):
        return self.cardString

class Round():
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def __repr__(self):
        return "P1: " + self.p1.__repr__() + " | P2: " + self.p2.__repr__()

    def determineWinner(self):
        pass

class Hand():
    def __init__(self, L):
        self.cards = list()

        for cS in L:
            self.cards.append(Card(cS))

        self.cards = sorted(self.cards)

    def card(self, index):
        return self.cards[index].num

    def suit(self, index):
        return self.cards[index].suit

    def highestRank(self):


    def __repr__(self):
        s = ""

        for card in self.cards:
            s += card.__repr__() + " "

        return s

    def royalFlush(self):
        if self.card(0) != 10:
            return (False,)

        suit = self.suit(0)

        results = map(lambda x: self.card(x)==x+10 and self.suit(x)==suit, range(1, 5))

        if all(results):
            return (True, suit)

        return (False,)

    def straightFlush(self):
        initial = self.card(0)

        suit = self.suit(0)

        results = map(lambda x: self.card(x)==x+initial and self.suit(x)==suit, range(1, 5))

        if all(results):
            return (True, initial, suit)

        return (False,)

    def fourOfKind(self):
        s = set([i.num for i in self.cards])

        if len(s) != 2:
            return (False,)

        first, second, third = self.card(0), self.card(1), self.card(2)

        if first == second or first == third:
            return (True, first)

        return (True, second)





def parseFile():
    filename = "p054_poker.txt"

    hands = list()

    with open(filename, "r") as f:
        lines = f.readlines()

        for line in lines:
            s = line.strip().split(" ")

            p1, p2 = Hand(s[:5]), Hand(s[5:])

            r = Round(p1, p2)

            hands.append(r)

    return hands

def runner():
    hands = parseFile()
    p1wins = 0

    for hand in hands:
        if hand.determineWinner() == PLAYER_1:
            p1wins += 1

    print p1wins

runner()




