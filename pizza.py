#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021
# This program calculates the cost of a pizza with tax

import constants


def main():
    # This program calculates the cost of a pizza with tax

    # input
    diameter = int(input("Please enter the diameter of the pizza (inch): "))

    # process
    subtotal = (
        constants.LABOR + constants.RENT + (diameter * constants.MATERIALS)
    )

    total = subtotal + (subtotal * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
