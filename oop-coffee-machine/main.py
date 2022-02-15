from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choiсe = input(f"What would you like ({coffee_menu.get_items()})? ")
    if choiсe == "report":
        coffee_maker.report()
        money_machine.report()
    elif choiсe == "off":
        is_on = False
    else:
        drink = coffee_menu.find_drink(choiсe)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

