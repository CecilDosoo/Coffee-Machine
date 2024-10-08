from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drinks = menu.get_items()

game = True

while game:
    choice = input(f"What would you like? {drinks}: ")
    if choice == "off":
        game = False
    elif choice == "report":
        coffee_maker.report(), money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
