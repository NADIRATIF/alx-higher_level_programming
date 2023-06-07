#!/usr/bin/python3
def print_last_digit(number):
    lastNumber = abs(number) % 10
    print(lastNumber, end=(""))
    return lastNumber
