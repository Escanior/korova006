from card import Card

def test_card_value_55():
    card = Card(55)
    assert card.point == 7

def test_card_value_divisible_by_11():
    card = Card(22)
    assert card.point == 5

def test_card_value_divisible_by_10():
    card = Card(30)
    assert card.point == 3

def test_card_value_divisible_by_5():
    card = Card(25)
    assert card.point == 2

def test_card_value_not_special():
    card = Card(7)
    assert card.point == 1