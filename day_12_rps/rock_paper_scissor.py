import random

hands = ['r', 'p', 's']
winning_combinations = [['r', 's'], ['p', 'r'], ['s', 'p']]


def random_throw():
    c = random.choice(hands)
    p = input("r, p, s?: ")
    print(c)
    choices = [[c, p]]
    if c == p:
        print("unentschieden.")
    if choices in winning_combinations:
        print("C wins")
    else:
        print("P wins")

random_throw()