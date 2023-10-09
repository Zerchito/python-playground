from deck import Deck
from hand import Hand
from chip import Chip
from helpers import take_bet, push, player_wins, show_some, player_busts, hit, dealer_busts, dealer_win, show_all

def hit_or_stand(deck, hand):
  global playing

  while True:
    x = input("Hit or Stand? Enter h or s")

    if x[0].lower() == 'h':
      hit(deck, hand)
    elif x[0].lower() == 's':
      print("Player stands. Dealer is playing")
      playing = False
    else:
      print("Sorry, please try again")
      continue
    break


while True:
  print('Welcome to BlackJack')
  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())


  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  player_chips = Chip()

  take_bet(player_chips)

  show_some(player_hand, dealer_hand)

  playing = True

  while playing:
    hit_or_stand(deck, player_hand)
    show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
      player_busts(player_hand, dealer_hand, player_chips)
      break
  
  if player_hand.value <= 21:

    while dealer_hand.value < 17:
      hit(deck, dealer_hand)

    show_all(player_hand, dealer_hand)

    if dealer_hand.value > 21:
      dealer_busts(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value > player_hand.value:  
      dealer_win(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand, dealer_hand, player_chips)
    else:
      push(player_hand, dealer_hand)

  print('\n Player total chips are at: {}'.format(player_chips.total))

  new_game = input('Would you like to play another hand? y/n')

  if new_game[0].lower() == 'y':
    playing = True
  else:
    print('Thank you for playing!')
    break