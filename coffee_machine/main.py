MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(choice):
    check = True
    for ingredient in MENU[choice]['ingredients']:
        if resources[ingredient] < MENU[choice]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            check = False
    return check


def process_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.5 + pennies * 0.01


def make_an_order(coffee):
    resources['money'] += MENU[coffee]['cost']
    for ingredient in MENU[coffee]['ingredients']:
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]


def check_pay(coffee, money):
    if money >= MENU[coffee]['cost']:
        make_an_order(coffee)
        print(f"Here is ${money} in change.")
        print(f"Here is your {coffee} ☕️.Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice in MENU:
            if check_resources(choice):
                check_pay(choice, process_coins())
        elif choice == "report":
            print_resources()
        elif choice == "off":
            is_on = False
        else:
            print("Error, enter something else")


if __name__ == "__main__":
    coffee_machine()