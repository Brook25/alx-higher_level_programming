#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)
    tuple1 = tuple_a
    tuple2 = tuple_b
    tuple = ()
    if length1 == 1:
        tuple1 += 0,
    elif length1 == 0:
        tuple1 = (0, 0)
    if length2 == 1:
        tuple2 += 0,
    elif length2 == 0:
        tuple2 = (0, 0)
    for i in range(2):
        tuple += (tuple1[i] + tuple2[i]),
    return tuple
