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
}


def ask_choice():
    while True:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        if choice in MENU or choice == "off" or choice == "report":
            return choice
        else: 
            print("\n***Invalid choice. Available options are:"
            " espresso/latte/cappuccino")


def show_report():
    print(f"\n--Water: {resources['water']}ml")
    print(f"--Milk: {resources['milk']}ml")
    print(f"--resources: {resources['coffee']}g")
    print(f"--Money: ${money}")


def check_resources(coffee):
    for resource, ammount in MENU[coffee]["ingredients"].items():
        if ammount > resources[resource]:
             print(f"Sorry there is not enough {resource}.")
             return False
    return True


def process_coins(coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if total >= MENU[coffee]["cost"]:
        global money
        money += MENU[coffee]["cost"]
        if total > MENU[coffee]["cost"]:
            change = total - MENU[coffee]["cost"]
            print(f"\n***Here is ${change:.2f} in change.")
        return True
    print("\n***Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(coffee):
    for resource, ammount in MENU[coffee]["ingredients"].items():
        resources[resource] -= ammount

money = 0

while True:
    command = ask_choice()

    if command == "off":
        print("\n***Sutting down...\n")
        break
    elif command == "report":
        show_report()
    elif check_resources(command) and process_coins(command):
        make_coffee(command)
        print(f"\n***Here is your {command}. Enjoy!")
