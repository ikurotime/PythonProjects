from data import MENU, resources

available_water = resources['water']
available_coffee = resources['coffee']
available_milk = resources['milk']
money = resources['money']
while 1:
    user_answer = input('What would you like? (espresso/latte/cappuccino):')
    if user_answer == 'report':
        print(f"Water: {available_water}ml \n"
              f"Milk: {available_milk}ml \n"
              f"Coffee: {available_coffee}g \n"
              f"Money: ${money}")
    elif user_answer == 'off':
        print('Turning off...')
        exit()
    else:
        cost = MENU[user_answer]['cost']
        required_water = MENU[user_answer]['ingredients']['water']
        required_coffee = MENU[user_answer]['ingredients']['coffee']
        required_milk = MENU[user_answer]['ingredients']['milk']

        if required_water > available_water:
            print("Sorry, there's not enough water")
        else:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

            if cost > total_amount:
                print("Sorry that's not enough money. Money refunded.")
            else:
                refund = total_amount - cost
                money += cost
                available_water -= required_water
                available_coffee -= required_coffee
                available_milk -= required_milk
                print(f"Here is ${round(refund,2)} in change!\n"
                      f"Here is your {user_answer} ☕ Enjoy!")
