from data import resources, coffee
from coffee_machine_functions import *

operating = True
while operating:
    choice = input("What would you like? (espresso/latte/cappucino): ")

    if choice == "report":
        show_report(resources)

    elif choice == "off":
        print("Powering down...")
        operating = False

    elif choice == "espresso" or choice == "latte" or choice == "cappucino":
        coffee_choice = choice

        if (check_resource(coffee_choice)):
            coffee_price = coffee[coffee_choice]['cost']
            print(f"Your total is ${coffee_price}")
            user_coins_amount = insert_coins()

            if user_coins_amount == coffee_price:
                print(f"Here is your {coffee_choice}!")

            elif user_coins_amount > coffee_price:
                change = calculate_change(coffee_price, user_coins_amount)
                print(f"Here is your change: ${change}")
                print(f"Here is your {coffee_choice}!")
                resources = update_resources(coffee_choice, resources)
                
            else:
                print(f"You dont have enough money")

        else:
            print("Not enough resources, Sorry!")
            