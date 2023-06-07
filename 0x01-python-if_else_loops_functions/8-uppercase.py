#!/usr/bin/python3
def uppercase(str):
    u = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            u += chr(ord(c) - 32)
        else:
            u += c
    print("{:s}\n".format(u), end=(""))
