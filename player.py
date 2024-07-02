class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.cards.pop(0))
