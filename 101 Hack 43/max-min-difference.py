#!/bin/python

import sys

filename = sys.argv[1]
with open(filename) as f:
	n = int(f.readline().strip())
	a = map(int,f.readline().strip().split(' '))
# input is at least length 3

# 7 4 3 1 3
# 4 3 1 3: diff = 3
# 7 4 3 3: diff = 4
# one pass: look for numbers that occur once
# second pass: for each number that occurs once, delete it. Find the max difference without it. What is the result?
# this is O(n^2)

# 5 4 0 8 3 8 4 1 1 8
# second pass: 5 4 0 3 4 1
# find the max of the repeats, find the min of the repeats
# find the max of the singleton, find the min of the singleton
# compare max of singleton to min of repeat
# compare min of singleton to max of repeat

count_dict = {}
for value in a:
    if value not in count_dict:
        count_dict[value] = 1
    else:
        count_dict[value] += 1
        
single_list = []
repeaters_list = []
for key in count_dict:
    if count_dict[key] > 1:
        repeaters_list.append(key)
    else:
        single_list.append(key)
        
        
single_min = max(a)
single_second_min = single_min

single_max = min(a)
single_second_max = single_max
for ele in single_list:
    if ele < single_min:
        single_second_min = single_min
        single_min = ele
    elif ele < single_second_min:
        single_second_min = ele
    if ele > single_max:
        single_second_max = single_max
        single_max = ele
    elif ele > single_second_max:
        single_second_max = ele

if len(repeaters_list) == 0:
	# we can either delete max or min single value!
	# which one we actually choose depends on the others.
	del a[a.index(single_max)]
	max_val = max(a)
	min_val = min(a)
	diff_a = abs(max_val - min_val)
	a.append(single_max)
	del a[a.index(single_min)]
	max_val = max(a)
	min_val = min(a)
	diff_b = abs(max_val - min_val)
	print min([diff_a, diff_b])
	
else:
    repeaters_min = min(repeaters_list)
    repeaters_max = max(repeaters_list)    
    diff_one = abs(repeaters_max - single_min)
    diff_two = abs(single_max - repeaters_min)
    diff_three = abs(single_max - single_min)

    #find the max of the above three
    # that number in single is what to remove
    # if diff_three is max, we can remove either single_max or single_min. so don't consider it!

    diff_max = max([diff_one, diff_two, diff_three])

    #print diff_max
    #print diff_one, diff_two, diff_three
    if diff_max == diff_one:
        del a[a.index(single_min)]
        max_val = max(a)
        min_val = min(a)
        print abs(max_val - min_val)

    elif diff_max == diff_two:
        del a[a.index(single_max)]
        max_val = max(a)
        min_val = min(a)
        print abs(max_val - min_val)    
    elif diff_max == diff_three:
		del a[a.index(single_max)]
		max_val = max(a)
		min_val = min(a)
		diff_a = abs(max_val - min_val)
		a.append(single_max)
		del a[a.index(single_min)]
		max_val = max(a)
		min_val = min(a)
		diff_b = abs(max_val - min_val)
		print min([diff_a, diff_b])   