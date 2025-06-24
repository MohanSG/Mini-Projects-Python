from ascii_cards.cards import print_card
from blackjack_art import art
import random
import os

player_value = 0
dealer_value = 0

player_cards = {}
dealer_cards = {}

cards_dealt = False
suits ={'spades':'♠','hearts':'♥','diamonds':'♦','clubs':'♣'}

def get_card_rank():
    rank = random.randint(2, 15)

    if rank <= 10:
        return int(rank)
    elif rank <= 13:
        return random.choice(['J', 'Q', 'K'])
    else:
        return 'A'

def get_card_values(dealer_or_player):
    hand_cards = {}
    hand_value = 0

    if dealer_or_player == "player":
        hand_cards = player_cards
    elif dealer_or_player == "dealer":
        hand_cards = dealer_cards

    for key in hand_cards:
        card_value = hand_cards[key][0] 

        if card_value != 'J' and card_value != 'Q' and card_value != 'K' and card_value != 'A':
            hand_value += int(hand_cards[key][0])
        elif card_value == 'J' or card_value =='Q' or card_value == 'K':
            hand_value += 10
        else:
            hand_value += 11
        
    for key in hand_cards:
        if 'A' in str(hand_cards[key][0]) and hand_value > 21:
            hand_value -= 10

    return hand_value
            
def get_a_card(dealer_or_player):
    global player_value
    global dealer_value

    random_suit = random.choice(list(suits.keys()))
    random_card_number = get_card_rank()
    if dealer_or_player == "player":
        player_cards[f'card{str(len(player_cards)+1)}'] = [random_card_number, suits[random_suit]]
        player_value = get_card_values("player")
    elif dealer_or_player == "dealer":
        dealer_cards[f'card{str(len(dealer_cards)+1)}'] = [random_card_number, suits[random_suit]]
        dealer_value = get_card_values("dealer")
    
def deal_cards():
    for _ in range(1,3):
        get_a_card("player")
    
    get_a_card("dealer")

def show_cards():
    os.system('cls')
    print("***** DEALERS CARDS *****")
    for key in dealer_cards:
        print_card(str(dealer_cards[key][0]), str(dealer_cards[key][1]))
    print(f"Dealer card value: {dealer_value}")
    print("***** PLAYERS CARDS *****")
    for key in player_cards:
        print_card(str(player_cards[key][0]), str(player_cards[key][1]))
    print(f"Player card value: {player_value}")

def main():
    global player_cards
    global dealer_cards
    global player_value
    global dealer_value 
    
    keep_playing = True
    while keep_playing:
        os.system('cls')
        print(art)
        play = input("Would you like to play a game of BlackJack? y/n: ").lower()
        os.system('cls')

        player_choice = ''
        game_not_ended = True

        if play == 'y':
            deal_cards()
            show_cards()

            if player_value == 21:
                game_not_ended = False
                print("YOU WIN") 

            while game_not_ended:
                player_choice = input("Hit or Stand?: ").lower()
                if player_choice == "hit":
                    get_a_card("player")
                    show_cards()
                    if player_value > 21:
                        game_not_ended = False
                        print("BUST")
                    elif player_value == 21:
                        print("YOU WIN")
                        game_not_ended = False
                elif player_choice == "stand":
                    get_a_card("dealer")
                    show_cards()
                    if dealer_value > 21:
                        game_not_ended = False
                        print("YOU WIN")
                    elif dealer_value <= 16:
                        while dealer_value <= 16:
                            get_a_card("dealer")
                            show_cards()
                    if dealer_value > 21 or player_value > dealer_value:
                            print("YOU WIN")
                            game_not_ended = False
                    elif dealer_value > player_value or dealer_value == 21:
                            print("DEALER WINS")
                            game_not_ended = False
                    elif player_value == dealer_value:
                                print("DRAW")
                                game_not_ended = False

            os.system('pause')
            player_value = 0
            dealer_value = 0
            player_cards = {}
            dealer_cards = {}

if __name__ == "__main__":
    main()
