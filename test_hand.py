import pytest

from hand import Hand
from card import Card

def test_init():
    hand = Hand(Card(5), Card(10))
    assert hand.cards == [5, 10]

def test_add_card():
    hand = Hand(Card(2))
    hand.add_card(Card(7))
    assert hand.cards == [2, 7]

def test_remove_card():
    hand = Hand(Card(3), Card(8))
    hand.remove_card(Card(3))
    assert hand.cards == [8]