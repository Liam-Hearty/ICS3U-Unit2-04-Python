#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program will calculate the cost of a diameter determined pizza.

import constants


def main():
    # this function will calculate the cost of the pizza

    # input
    diameter = int(input("Enter the diameter of the pizza you would " +
                         "like (in inches): "))

    # process
    sub_total = constants.LABOR + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
