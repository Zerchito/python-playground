suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
         'Ten', 'Jack', 'Queen', 'king', 'Ace')
values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'king': 10,
          'Ace': 11 }

def take_bet(chips):
  while True:
    try:
      chips.bet = int(input("How many chips would you like to bet?"))
    except:
      print("Sorry, a bet must be an integer")
    else:
      if chips.bet > chips.total:
        print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
      else:
        break

def hit(deck, hand):
  single_card = deck.deal()
  hand.add_card(single_card)
  hand.adjust_for_ace()

def show_some(player, dealer):

  print("\n Dealer's Hand:")
  print("First card hidden!")
  print(dealer.cards[1])

  print("\b Player's hand:")
  for card in player.cards:
    print(card)

def show_all(player, dealer):
    
  print("\n Dealer's Hand:")
  for card in dealer.cards:
    print(card)
  
  print(f"Value of Dealer's hand is: {dealer.value}")
  print("\n Player's hand:")
  for card in player.cards:
    print(card)
  print(f"Value of Dealer's hand is: {player.value}")

def player_busts(player, dealer, chips):
  print('BUST PLAYER!')
  chips.lose_bet()

def player_wins(player, dealer, chips):
  print('PLAYER WINS!')
  chips.lose_bet()

def dealer_busts(player, dealer, chips):
  print('PLAYER WINS!, DEALER BUSTED!')
  chips.lose_bet()

def dealer_win(player, dealer, chips):
  print('DEALER WINS!')
  chips.lose_bet()

def push(player, dealer):
  print('Dealer and player tie!. Push')