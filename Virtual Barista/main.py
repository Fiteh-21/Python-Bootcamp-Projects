from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_obj = CoffeeMaker()
money_obj = MoneyMachine()
menu_obj = Menu()
off_machine = False


while not off_machine:
    options = menu_obj.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
         off_machine = True
    elif choice == "report":
        coffee_obj.report()
        money_obj.report()
    else:
        drink = menu_obj.find_drink(choice)
        if coffee_obj.is_resource_sufficient(drink) and money_obj.make_payment(drink.cost):
                coffee_obj.make_coffee(drink)

