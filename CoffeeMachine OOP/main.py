from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coin = MoneyMachine()
menu =  Menu()

while 1:
    selected_drink = input('What would you like? (espresso/latte/cappuccino/): ')
    drink = menu.find_drink(selected_drink)
    if selected_drink == 'report':
        coffee_machine.report()
        coin.report()
    elif selected_drink == 'off':
        print('Shutting down...')
        exit()
    elif coffee_machine.is_resource_sufficient(drink):
        if coin.make_payment(drink.cost) == True:
            coffee_machine.make_coffee(drink)