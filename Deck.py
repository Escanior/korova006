import random
class Deck:
    def __init__(self):
        self.cards = [Card(i) for i in range(104)]

    def shuffle(self):
        random.shuffle(self.cards)