#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            val = val1 / val2
        except IndexError:
            print("out of range")
            val = 0
        except TypeError:
            print("wrong type")
            val = 0
        except ZeroDivisionError as err:
            print(str(err))
            val = 0
        except ValueError:
            val = 0
        finally:
            new_list += [val]
    return new_list
