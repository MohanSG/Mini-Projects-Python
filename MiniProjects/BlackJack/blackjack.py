from ascii_cards.cards import print_card
import random

player_cards = {}
player_value = 0

dealer_cards = {}
dealer_value = 0

suits ={'spades':'♠','hearts':'♥','diamonds':'♦','clubs':'♣'}

def deal_cards():
    keys = list(suits.keys())
    random_key = random.choice(keys)

def get_card_rank():
    rank = random.randint(1, 15)

    if rank <= 10:
        return int(rank)
    elif rank <= 13:
        return random.choice(['J', 'Q', 'K'])
    else:
        return 'A'
    
def deal_initial_cards():
    for card in range(1,3):
        random_suit = random.choice(list(suits.keys()))
        random_card_number = get_card_rank()
        player_cards['card1'] = random_card_number, suits[random_suit]
    
    return print_card(str(player_cards['card1'][0]), player_cards['card1'][1])
    
deal_initial_cards()