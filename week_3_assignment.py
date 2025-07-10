#!/usr/bin/env python3
""" This module contains a function calculate_discount """


original_price = int(input("Enter the price of your item: "))
discount_percent = input("Enter the discount percentage: ")
discount = discount_percent[:-1]
discountprice = int(discount)


def calculate_discount(price, discount_percent):
    """ Gives the price after discount has been applied """
    return price - (price * discount_percent) / 100


print(calculate_discount(original_price, discountprice))
