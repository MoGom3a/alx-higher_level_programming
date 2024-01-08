#!/usr/bin/python3
def no_c(my_string):
    cnull = ""
    for ind in range(len(my_string)):
        if (my_string[ind] != 'c' and my_string[ind] != 'C'):
            cnull += my_string[ind]
    return cnull
