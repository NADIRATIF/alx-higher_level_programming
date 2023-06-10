#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [False] * len(my_list)

    for item in range(len(my_list)):
        if my_list[item] % 2 == 0:
            new_list[item] = True
    return new_list
