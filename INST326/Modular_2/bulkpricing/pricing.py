""" Calculate the price of an order of magnets according to a bulk
pricing scheme. """

import sys


def get_cost(quantity):

    if (quantity < 50):
        price = 0.75
    elif (quantity >= 50):
        price = 0.72
    elif (quantity >= 100 and quantity <= 999):
        price = 0.70
    else:
        price = 0.67

    cost = quantity * price
    return cost


if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))