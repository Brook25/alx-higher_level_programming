#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for elem in my_list:
        try:
            if x == j:
                break
                print(elem, end="")
        except IndexError:
            print("Error")
        j += 1
    print()
    return j
