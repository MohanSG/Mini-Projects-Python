import os
from hammerart import art

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def find_highest_bidder(bids):
    highest_bid = 0
    for key in bids:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            highest_bidder = key
    print(f"The highest bider is {key} with a bid of {bids[key]}")

blind_bids = {}
highest_bidder = ''
print(art+ "\n")
bidding = True

while bidding:        
    name = input("What is your name? \n")
    bid = int(input("Place your bid: \n$"))

    blind_bids[name] = bid
    print(blind_bids)

    continue_bidding = input("Are there any more bidders? (yes or no)\n").lower()

    if continue_bidding == "no":
        bidding = False
        find_highest_bidder(blind_bids)

    elif continue_bidding == "yes":
        clear_terminal()
    else:
        print("Invalid option: Please type yes or no")