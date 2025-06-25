from gamedata import data
from gameart import art
import random
import os

def get_random_insta(data):
    return data[random.randint(0, len(data) - 1)]

def check_choice(player_choice, other_choice):
    if player_choice > other_choice:
        return True
    elif other_choice > player_choice:
        return False
    
card_a = get_random_insta(data)
card_b = get_random_insta(data)

os.system('cls')
print(art)

print(f"Compare A: {card_a['name']}, a {card_a['description']}, from {card_a['country']}")
print('vs.')
print(f"Compare A: {card_b['name']}, a {card_b['description']}, from {card_b['country']}")

player_choice = input('Who has more followers? Type "A" or "B": ')
