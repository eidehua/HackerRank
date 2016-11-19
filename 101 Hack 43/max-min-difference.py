#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
# input is at least length 3

# 7 4 3 1 3
# 4 3 1 3: diff = 3
# 7 4 3 3: diff = 4
# one pass: look for numbers that occur once
# second pass: for each number that occurs once, delete it. Find the max difference without it. What is the result?
# this is O(n^2)

# 5 4 0 8 3 8 4 1 1 8

# Given any list, we have a Max value, and a Min value.
# Remove one of these, to reduce the maximum difference between the new max, min pair
# So we need to compare the differences: (max-second min) and (second max - min), see which is smaller. This is the new smallest max-min difference

max_val = -sys.maxint
second_max = -sys.maxint

min_val = sys.maxint
second_min = sys.maxint

for value in a:
    # found a new minimum.
    if value < min_val:
        second_min = min_val
        min_val = value
    elif value < second_min:
        second_min = value
    if value > max_val:
        second_max = max_val
        max_val = value
    elif value > second_max:
        second_max = value

diff_remove_min = max_val - second_min
diff_remove_max = second_max - min_val

print diff_remove_min if diff_remove_min < diff_remove_max else diff_remove_max

# C++: value = a > 10 ? b : c
#   aka if a is greater than 10, value is b. Otherwise, value is c
# Python: value= b if a > 10 else c
#   aka value is b if a is greater than 10, else it is c
