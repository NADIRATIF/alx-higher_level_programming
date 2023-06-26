#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    rl = []

    try:
        for i in range(list_length):
            try:
                a = my_list_1[i]
                b = my_list_2[i]
                r = a / b
                rl.append(r)
            except ZeroDivisionError:
                rl.append(0)
                print("division by 0")
            except (TypeError, IndexError):
                rl.append(0)
                if len(my_list_1) <= i or len(my_list_2) <= i:
                    print("out of range")
                else:
                    print("wrong type")
    finally:
        return rl
