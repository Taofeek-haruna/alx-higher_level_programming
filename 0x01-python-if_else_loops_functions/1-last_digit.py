#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

# YOUR CODE HERE

print('Last digit of', number, 'is', number[-1]\n)
if number[-1] > 5:
    print('and is greater than 5\n')

elif number[-1] == 0:
    print('and is 0\n')

elif number[-1] < 6, != 0:
    print('and is less than 6 and not 0\n')
