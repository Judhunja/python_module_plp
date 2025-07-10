#!/usr/bin/env python3

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operations = input(
    "What operation would you like to do with the numbers? Options: +, -, /, * / ")

if operations == '+':
    print(number1 + number2)
elif operations == '-':
    print(number1 - number2)
elif operations == '/':
    print(number1 / number2)
elif operations == '*':
    print(number1 * number2)
