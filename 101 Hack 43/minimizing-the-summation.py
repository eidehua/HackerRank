#!/bin/python

import sys

filename = sys.argv[1]
with open(filename) as f:
	n,k = f.readline().strip().split(' ')
	n,k = [int(n),int(k)]
	a = map(int,f.readline().strip().split(' '))

'''
We simplify the equation to:
(A) = 2*k*sum(b_i^2) - 2*sum(b_i)^2

So we only need to keep track of sum(b_i^2) and sum(b_i)
'''

'''
So after sorting the list a_0 to a_n-1 in ascending order

There is a set of k CONSECUTIVE numbers that will minimize the summation.
    Since our list is sorted, k consecutive numbers would minimize the summation. if you included a non-consecutive number, it would be farther away than the consecutive number!

We need to find this set of k greedily
So first just consider the value of (A) for the first k elements of the list

REMEMBER: HAS TO BE A SET OF K CONSECUTIVE NUMBERS.
So we compare the value of (A) of elements at index {0, k}
Then the value of (A) of elements at index {1, k+1}
    if the summation (A) of {0,k} is smaller:
        compare {0,k} summation with {2, k+2} summation
    elif summation of {1, k+1} is smaller:
        comapre summation {1, k+1} with {2, k+2}

'''
# So, in the end, we find the best set of K consecutive numbers that minimzies (A) in ONE PASS.
# Note, we need the property of consecutive numbers to achieve the O(n) time to find the set
# Overall runtime is O(nlogn) because of the initial sort

# Much of the problem is being able to break the initial equation down to a form that allows us to just keep track of
# CHECK THE HELPER PNG for math breakdown
# sum(b_i^2) and sum(b_i) of k consecutive numbers. 
# Then it becomes a greedy algorithm which is simple to solve


sorted_list = sorted(a)
sum_a = 0                                       # keep track of sum(b_i^2)
sum_b = 0                                       # keep track of sum(b_i)
sum = 0                                         # keep track of entire summation
for i in xrange(0, k):
    b_i = sorted_list[i]
    sum_a += b_i**2
    sum_b += b_i
sum = 2*k*sum_a - 2*sum_b**2

# consider {1,k+1}, {2, k+2}, ..., { n-1-k ,n-1}
for i in xrange(k, n):
    b_i = sorted_list[i]
    element_to_kick_out = sorted_list[i - k]    # If we consider element k, Need to remove element 0
    sum_a += b_i**2 - element_to_kick_out**2
    sum_b += b_i - element_to_kick_out
    sum = min(sum, 2*k*sum_a - 2*sum_b**2)
print sum