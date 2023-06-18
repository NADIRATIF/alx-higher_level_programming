#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    s_p = 0
    s_w = 0
    for s, w in my_list:
        s_p += s * w
        s_w += w
    return s_p / s_w
