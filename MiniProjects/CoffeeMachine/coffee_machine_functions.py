from data import resources, coffee

def show_report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def sufficient_user_balance(balance, price):
    if balance < price:
        False
    else:
        True
        
def check_resource(coffee_to_make, resources):
    coffee_choice = coffee[coffee_to_make]

    if coffee_choice['water'] <= resources['water'] and coffee_choice['milk'] <= resources['milk'] and coffee_choice['coffee'] <= resources['coffee']:
        return True
    else:
        return False
    
def insert_coins():
    total = 0

    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickles?: "))
    pennies = float(input("How many pennis?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    return round(total, 2)

def calculate_change(coffee_price, coins):
    return round(coins - coffee_price, 2)

def update_resources(coffee_made, resources):
    
    milk_used = coffee[coffee_made]['milk']
    water_used = coffee[coffee_made]['water']
    coffee_amount_used = coffee[coffee_made]['coffee']
    coffee_price = coffee[coffee_made]['cost'] 
    
    updated_resources =  {
        "water": resources['water'] - water_used,
        "milk": resources['milk'] - milk_used,
        "coffee": resources['coffee'] - coffee_amount_used,
        "money": resources['money'] + coffee_price
    }
    
    return updated_resources