#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for elem in my_list:
        try:
            j += 1
            if x >= j:
                print(elem, end="")
        except IndexError:
            print("Error")
    print()
    return j
