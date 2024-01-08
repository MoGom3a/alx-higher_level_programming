#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_f = tuple_a[0] if len(tuple_a) > 0 else 0
    a_s = tuple_a[1] if len(tuple_a) > 1 else 0
    b_f = tuple_b[0] if len(tuple_b) > 0 else 0
    b_s = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a_f + b_f, a_s + b_s)
