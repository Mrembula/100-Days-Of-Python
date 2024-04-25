from coffee_machine import MENU
from coffee_machine import resources


def coffee(customer_choice):
    """Returns user choice"""
    return MENU[customer_choice]


def check_resources(customer_option, machine_resources):
    count = 0
    """Checks the ingredients are still available for making coffee return one if true"""
    for ingredient in customer_option:
        negative_number = machine_resources[ingredient] - customer_option[ingredient]
        if negative_number < 0:
            print(f"Sorry there is not enough {ingredient}")
            count += 1

    return count


def user_coins():
    """resources are sufficient coffee machine should print the amount of quarter, dimes and pennies and nickels
    to insert returns an array of amount"""
    print("\nPlease insert coins")
    coins = ['quarters', 'dimes', 'nickels', 'pennies']
    insert_coins = []
    for coin_type in coins:
        insert_coins.append(int(input(f"How many {coin_type}?: ")))

    return insert_coins


def calculate(inserted_coins):
    """Calculates the amount user inserted returns the total """
    coin_calculate = [0.25, 0.10, 0.05, 0.01]
    total_amount = 0
    for i in range(0, len(inserted_coins) - 1):
        total_amount += inserted_coins[i] * coin_calculate[i]

    return total_amount


def report(coffee_ingredients, coffee_machine_resources):
    """Removes the amount of ingredients after user purchase returns a dictionary or remaining
    ingredients"""
    coffee_machine_resources['water'] -= coffee_ingredients['water']
    coffee_machine_resources['coffee'] -= coffee_ingredients['coffee']
    if coffee_machine_resources['milk'] in coffee_machine_resources:
        coffee_machine_resources['milk'] -= coffee_ingredients['milk']

    return coffee_machine_resources


machine_on = True
while machine_on:
    customer_input = input("What would you like to? (expresso/latte/cappuccino): ").lower()

    '''create a check button to display the users order and what they're requesting'''
    option = coffee(customer_input)
    if len(option['ingredients']) == 4:
        print(
            f"Water: {option['ingredients']['water']}ml\nMilk: {option['ingredients']['milk']}ml\nCoffee: {option['ingredients']['coffee']}g\nMoney: ${option['cost']}")
    else:
        print(
            f"Water: {option['ingredients']['water']}ml\nCoffee: {option['ingredients']['coffee']}ml\nMoney: ${option['cost']}")

    '''
    else the coffee machine should write a message to the user telling the user insufficient ingredients'''
    count_no = check_resources(option['ingredients'], resources)
    if count_no > 0:
        break

    coins = user_coins()
    total = calculate(coins)

    change = total - option['cost']
    if change > 0:
        print(f"\nHere is ${change:.2f} dollars in change")
    else:
        print(f"\nSorry that's is not enough money. Money refunded")

    option = report(option['ingredients'], resources)

    print(f"Here is your {customer_input}. Enjoy!")

    off_status = input("1.prompt 'off' to turn off\n2.Check 'report' to check report\n").lower()
    if off_status == 'off':
        machine_on = False
    elif off_status == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n")


