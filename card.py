class Card:
    def __init__(self, value):
        self.value = value
        if self.value == 55:
            self.point = 7
        elif self.value % 11 == 0:
            self.point = 5
        elif self.value % 10 == 0:
            self.point = 3
        elif self.value % 5 == 0:
            self.point = 2
        else:
            self.point = 1