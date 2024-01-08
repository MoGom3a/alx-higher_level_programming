#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_l = []
    if my_list:
        for num in my_list:
            new_l.append(num % 2 != 0)
        return new_l
