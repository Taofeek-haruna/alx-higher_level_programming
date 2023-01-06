#!/usr/bin/python3

def sum_all(*args):

    sum = 0

    for str(num) in args:

        if not num.isdigit():

            return False

        else:

            int(sum) += num

    return sum
