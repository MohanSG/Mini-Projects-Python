from ascii_cards.cards import print_card
import random

player_cards = {}
player_value = 0

dealer_cards = {}
dealer_value = 0

cards_dealt = False

suits ={'spades':'♠','hearts':'♥','diamonds':'♦','clubs':'♣'}

def get_card_rank():
    rank = random.randint(1, 15)

    if rank <= 10:
        return int(rank)
    elif rank <= 13:
        return random.choice(['J', 'Q', 'K'])
    else:
        return 'A'
    
def get_a_card(dealer_or_player):
    random_suit = random.choice(list(suits.keys()))
    random_card_number = get_card_rank()
    if dealer_or_player == "player":
        player_cards[f'card{str(len(player_cards)+1)}'] = [random_card_number, suits[random_suit]]
    elif dealer_or_player == "dealer":
        dealer_cards[f'card{str(len(dealer_cards)+1)}'] = [random_card_number, suits[random_suit]]


def deal_cards():
    for _ in range(1,3):
        get_a_card("player")
        get_a_card("dealer")

def show_cards():
    print("***** DEALERS CARDS*****")
    for key in dealer_cards:
        print_card(str(dealer_cards[key][0]), str(dealer_cards[key][1]))
    print("***** PLAYERS CARDS*****")
    for key in player_cards:
        print_card(str(player_cards[key][0]), str(player_cards[key][1]))

play = input("Would you like to play a game of BlackJack? y/n: ")
if play == 'y':
    deal_cards()
    cards_dealt = True
    show_cards()
