import coffee_data


def resources_check(request):
    """Checks if the resources available are enough to make the coffee."""
    for elem in coffee_data.MENU[request]['ingredients']:
        if coffee_data.resources[elem] < coffee_data.MENU[request]['ingredients'][elem]:
            print(f"Sorry there is not enough {elem}.")
            return False
    return True


coffee_data.resources['money'] = 0


def user_total_coins():
    """Process user coins.
    :rtype: total amount of coins paid by the user
    """
    print("Please insert coins.")
    coin_quarter = float(input("How many quarters?: ")) * 0.25
    coin_dime = float(input("How many dimes?: ")) * 0.10
    coin_nickle = float(input("How many nickles?: ")) * 0.05
    coin_pennies = float(input("How many pennies?: ")) * 0.01
    total_coins = coin_quarter + coin_dime + coin_nickle + coin_pennies
    if total_coins < coffee_data.MENU[user_request]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total_coins > coffee_data.MENU[user_request]['cost']:
        coin_refund = round(total_coins - coffee_data.MENU[user_request]['cost'], 2)
        print(f"Here is ${coin_refund} dollars in change.")
        coffee_data.resources['money'] = coin_refund
    else:
        coffee_data.resources['money'] = total_coins
    return True


should_continue = True
while should_continue:
    user_request = input("“What would you like? (espresso/latte/cappuccino): ").lower()
    if user_request == 'espresso' or user_request == 'latte' or user_request == 'cappuccino':
        if resources_check(user_request) and user_total_coins():
            for element in coffee_data.MENU[user_request]['ingredients']:
                coffee_data.resources[element] -= coffee_data.MENU[user_request]['ingredients'][element]
            print('Here is your latte. Enjoy!')
    elif user_request == 'report':
        print(f'Water:\t{coffee_data.resources["water"]}ml\n'
              f'Milk:\t{coffee_data.resources["milk"]}ml\n'
              f'Coffee:\t{coffee_data.resources["coffee"]}g\n'
              f'Money:\t${coffee_data.resources["money"]}')
    elif user_request == 'off':
        should_continue = False
    else:
        print("Invalid input. Please enter 'espresso', 'latte', 'cappuccino'.")
