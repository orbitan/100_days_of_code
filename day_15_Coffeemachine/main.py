from coffee_resources import *
import time


# Coffee Machine

#  Check if left overs differ from required amount
def sufficiency_check(customer_choice):
    if customer_choice in MENU:
        ingredients = (MENU[f'{customer_choice}']['ingredients'])
        for entry in ingredients:
            left_amount = left_overs[entry]
            required_amount = ingredients[entry]
            result = left_amount - required_amount
            if result < 0:
                print(f"There is not enough {entry} left.")
                break
            else:
                left_overs[entry] = result
                payment(customer_choice)


#  report, delivers resource values
def report():
    for _ in left_overs:
        print(f"{_}: {left_overs[_]}")


#  Ask User for wish (Espresse/latte/cappuccino)
def main_loop():
    while True:
        users_order = input("What would you like? (espresso/latte/cappuccino): ")
        sufficiency_check(users_order)
        #  Turn off Coffee Machine by entering "off"
        if users_order == "off":
            print("Machine is turning off now....")
            time.sleep(2.5)
            print("Good night")
            break
        elif users_order == "report":
            report()


#  Process Coins
def processing_coins():
    coins = ['Penny', 'Nickel', 'Dime', 'Quarter']
    worth = [0.01, 0.05, 0.10, 0.25]
    i = 0
    given_amount = 0
    while i <= 3:
            received = int(input(f"{coins[i]}: ")) * worth[i]
            if received != 0:
                given_amount = received + given_amount
            i += 1
    print(round(given_amount, 2))
    return given_amount


#  Check if users input represents the needed amount, refund if neccessary
def payment(customer_choice):
    cost = MENU[customer_choice]['cost']
    print(f"Your {customer_choice} makes {cost}$.")
    payed = processing_coins()
    if payed >= cost:
        print(f"Thank you for paying. You receive {(cost - payed) * -1}$.")
        main_loop()
    else:
        print("You little peace of shit didn't pay enough. You will get nothing back.")
        main_loop()





#  Make Coffee
main_loop()