class Card:
    suits = ["Spades","Hearts","Diamonds","Clubs"]
    values=[None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        if self.value <= other.value:
            return True
        if self.value==other.value:
            if self.suit<other.suit:
                return True
            else:
                return False
        return False
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value==other.value:
            if self.suit>other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        value=(self.values[self.value]+" of "+
               self.suits[self.suit])
        return value
