from gamedata import data
from gameart import art
import random
import os

def get_random_insta(data):
    """Returns a random instagram dictionary from 'data'

    Args:
        data (dictonary): a collection of instagram profiles

    Returns:
        dictionay : a dictionary of instagram profile info
    """
    return data[random.randint(0, len(data) - 1)]

def check_choice(player_choice, other_choice):
    if player_choice['follower_count'] > other_choice['follower_count']:
        return True
    elif other_choice['follower_count'] > player_choice['follower_count']:
        return False
    
card_a = get_random_insta(data)
card_b = get_random_insta(data)
score = 0

winning = True
while winning:

    os.system('cls')
    print(art)
    if score > 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {card_a['name']}, a {card_a['description']}, from {card_a['country']}")
    print('vs.')
    print(f"Compare B: {card_b['name']}, a {card_b['description']}, from {card_b['country']}")

    player_choice = input('Who has more followers? Type "A" or "B": ').lower()
    if player_choice == 'a':
        winning = check_choice(card_a, card_b)
    elif player_choice == 'b':
        winning = check_choice(card_b, card_a)

    if winning:
        score += 1
        card_a = card_b
        card_b = get_random_insta(data)
    else:
        os.system('cls')
        print(art)
        print(f"Sorry, thats wrong. Final score: {score}")
