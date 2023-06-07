#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b >= 0:
        for i in range(b):
            p *= a
    else:
        for i in range(abs(b)):
            p /= a
    if a < 0 and b < 0:
        return "{:.20e}".format(p)
    else:
        return p
