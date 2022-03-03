from coffee_maker import *
from menu import *
from money_machine import *

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main_loop():
    while True:
        order = input("Enter your choice (latte/espresso/cappuccino) : ")
        if order == "report":
            coffee_maker.report()
        else:
            drink = menu.find_drink(order)
            can_make = coffee_maker.is_resource_sufficient(drink)
            if can_make:
                print(drink.cost)
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)



                #coffee_maker.make_coffee(drink)

main_loop()