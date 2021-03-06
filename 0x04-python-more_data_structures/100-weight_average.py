#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    tot = 0
    div = 0
    for tup in my_list:
        j = 1
        for i in range(len(tup)):
            j *= tup[i]
        div += tup[1]
        tot += j
    return tot / div
