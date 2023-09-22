from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

x = Menu()
z = CoffeeMaker()
m = MoneyMachine()

should_continue = True
while should_continue:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        user_request = x.find_drink(order)
        if z.is_resource_sufficient(user_request):
            if m.make_payment(user_request.cost):
                z.make_coffee(user_request)
    elif order == 'report':
        z.report()
        m.report()
    elif order == 'off':
        should_continue = False
    else:
        print("Kindly place the correct order.")
