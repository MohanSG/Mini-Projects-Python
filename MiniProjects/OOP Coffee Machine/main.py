from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffee_Maker = CoffeeMaker()
Coffee_Menu = Menu()
Money_Machine = MoneyMachine()

operating = True
while operating: 
    choice = input(f"What would you like? ({Coffee_Menu.get_items()}): ")

    if choice == "report":
        Coffee_Maker.report()
        Money_Machine.report()
        
    elif choice == "off":
        operating = False
        print("Shutting down....")
        
    elif choice == "espresso" or choice == "latte" or choice =="cappuccino":
        chosen_coffee = Coffee_Menu.find_drink(choice)
        
        if Coffee_Maker.is_resource_sufficient(chosen_coffee):
            
            if Money_Machine.make_payment(chosen_coffee.cost):
                Coffee_Maker.make_coffee(chosen_coffee)
                
        else:
            print("Not enough resources. Sorry!")