#!/usr/bin/python3
<<<<<<< HEAD
def roman_to_int(roman_string):
    if type(roman_string) == str:
        sum_v = 0
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(roman_string)):

            if i == len(roman_string) - 1:
                sum_v += num[roman_string[i]]

            elif num[roman_string[i + 1]] <= num[roman_string[i]]:
                sum_v += num[roman_string[i]]

            else:
                sum_v -= num[roman_string[i]]

        return (sum_v)
    else:
        return (0)
=======
# -----------------------------------------------------------
# Python program that:
# how to convert a Roman numeral to an integer
# -----------------------------------------------------------


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_d[roman_string[j]] > roman_d[roman_string[j - 1]]:
            roman_n += roman_d[roman_string[j]] - 2 * \
                        roman_d[roman_string[j - 1]]
        else:
            roman_n += roman_d[roman_string[j]]
    return roman_n
>>>>>>> 4807dfd989bf83c163892ac93ae83e619d824e86
