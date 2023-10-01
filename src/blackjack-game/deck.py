import random
from card import suits, ranks, Card

class Deck:

  def __int__(self):

    self.all_cards = []

    for suit in suits:
      for rank in ranks: 
        #create the card
        created_card = Card(suit, rank)
        self.all_cards.append(created_card)
  
  def shuffle(self):
    random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()