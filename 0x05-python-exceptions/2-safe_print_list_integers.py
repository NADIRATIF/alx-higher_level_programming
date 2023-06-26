#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0

    try:
        for e in my_list:
            try:
                print("{:d}".format(e), end="")
                c += 1
            except ValueError:
                continue

            if c >= x:
                break

        print()
    except TypeError:
        pass

    return c
