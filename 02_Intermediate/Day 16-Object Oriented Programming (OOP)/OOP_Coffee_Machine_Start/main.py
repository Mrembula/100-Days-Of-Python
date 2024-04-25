from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
menu = Menu()
coffee_maker = CoffeeMaker()
current_money = MoneyMachine()
can_make = False
while on:
    while True:
        order = input(f"What would you like {menu.get_items()}: ").lower()

        if order == 'report':
            coffee_maker.report()
        elif order == 'off':
            break
        else:
            coffee = menu.find_drink(order)
            if not coffee:
                break
            can_make = coffee_maker.is_resource_sufficient(coffee)
            if not can_make:
                break

            payment = current_money.make_payment(coffee.cost)
            if not payment:
                break

            coffee_maker.make_coffee(coffee)

    make_coffee = input("Would you like some coffee today?: (Yes / No): ").lower()
    if make_coffee == 'no':
        on = False
