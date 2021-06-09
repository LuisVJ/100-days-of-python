from typing import Mapping
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
MACHINE = CoffeeMaker()
MONEY = MoneyMachine()

while True:
    choice = input(f"What would you like? {MENU.get_items()}:")
    if choice == "report":
        MACHINE.report()
        MONEY.report()
    elif choice == "off":
        break
    elif choice in MENU.get_items():
        drink = MENU.find_drink(choice)
        if MACHINE.is_resource_sufficient(drink) and MONEY.make_payment(drink.cost):
            MACHINE.make_coffee(drink)
