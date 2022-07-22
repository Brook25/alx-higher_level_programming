#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        val = a / b
        return a / b
    except ZeroDivisionError:
        val = None
        return val
    finally:
        print("Inside result: {}".format(val))
