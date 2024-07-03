class Hand:
    def __init__(self, *args):
        self.cards = []
        for i in args:
            self.cards.append(i.value)

    def add_card(self, card):
        self.cards.append(card.value)

    def remove_card(self, card):
        self.cards.remove(card.value)
