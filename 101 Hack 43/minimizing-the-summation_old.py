#!/bin/python

'''
Given n numbers, a0, a1, ..., an-1, choose exactly k numbers, b0, b1,..., bk-1, such that the value of ans below is minimal:

ans = sum_i sum_j (bi - bj)^2 for i,j in {0, k-1}

example
4 2
2 0 9 5

n = 4, k = 2
Pick {2, 0} to get (2-2)^2 + (2-0)^2 + (0-0)^2 + (0-2)^2 = (2-0)^2 + (0-2)^2 = 8

example
4 3
2 0 9 5
Pick {2, 0, 5} to get (2-5)^2 + (2-0)^2 + (0-2)^2 + (0-5)^2 + (5-2)^2 + (5-0)^2
    we can see this also as 2*(2-5)^2 + 2*(2-0)^2 + 2*(0-5)^2
    
    Seems like we want to choose the set, such that the differences between them are the minimum we can choose
    Eg Look at pairs:
        2,0 (diff 2)
        2,5 (diff 3)
        0,5 (diff 5)
    Compare it with chosing 2, 0, 9
        2, 0 (diff 2)
        2, 9 (diff 7)
        0, 9 (diff 9)
        
First algorithm idea:
Base case and build

k = 1
Can be any number!

k = 2
Pick the two closest numbers
{2,0}

k = 3
Add the number that is closest to both (to minimize squared difference)
{2,0} is original set
Check 5. 
    This is 3 away from 2, and 5 away from 0
Check 9.
    This is 7 awawy from 2, and 9 away from 0. Which would make the squared difference much worse
    
This should be a O(k^2*n) ~ O(n^3) algorithm

At step k imagine we have a set of numbers {x0,x1,...xk-2} representing the k-1 numbers we would pick.
    To add the kth number, we would have to run through array A, and find the element that contributes the least additional squared difference to all the numbers in the set.

    Step 1 takes 1*n work
    Step 2 takes 2*(n-1) work
    Step 3 takes 3*(n-2) work
    ...
    Step k-1 takes (k-1)*(n-k-2)
    Step k takes k*(n-k)
    
    
    So total effort is (1+2+3...+k)*n
    We know 1+2+3+...k = k(k+1)/2 = O(k^2)
    So Total algorithm is O(k^2 * n)
    
    Worst case: k = n, so O(n^3)
    
'''

'''
Previously at every step the algorithm was like this
Given the best set of (k-1) numbers S
Given the remaining array list of (n-(k-1)) numbers A
For every element a in A:
    compute the distance from every element in the set to a
add the element a that has the minimum distance from all elements

Improved algorithm:
What if we didn't have to compare every remaining element of a with k?
Given a best set of (k-1) numbers S, we only care about the min and max of this set.

The kth best number to add (to get the minimum squared distance), will the the one that is closest to the end points of the set

    Step 1 takes 1*n work
    Step 2 takes 1*(n-1) work
    ...
    Step k takes 1*(n-k) work
    
    0 < k <= n
    So worst time complexity is when we have k=n, so n*(n-1)*...*2*1 total work, which is O(n^2)
    Best time complexity is k = 1, with O(n) time
'''

'''
Next improved algorithm:

1. Sort
2. Find the two elements that are closest together. This is our (2) set
    3. Finding the third element is just finding the element to the left or to the right: which is closer.
    
4. Given a (k-1) set, specified by indices (L as left index, R as right index) in the array (allowed by our sorted structure)
    5. find the kth number, either L-1, or R+1
   
   Sort: O(nlogn)
   Loop: O(k) ~ O(n)
   
   Total runtime: O(nlogn)

   This idea is wrong! Because
   Say we have this:
   
   1 5 7 9 10 ........  100 101 110
   k = 3
   My algorithm will first find {100,101} And start expanding around that.
   It will then have {100, 101, 110} for k = 3
   
   But best 3 pair would be {5,7,9}
'''

import sys

filename = sys.argv[1]
with open(filename) as f:
	n,k = f.readline().strip().split(' ')
	n,k = [int(n),int(k)]
	a = map(int,f.readline().strip().split(' '))

# Minimal sum of squared difference of one element is just 0
if k == 1:
	print 0
else:
	#sort list
	sorted_list = sorted(a)
	# find the two elements closest to each other
	start_index = 0
	end_index = 1
	smallest_distance = abs(sorted_list[0] - sorted_list[1])
	# hits elements at index 1, 3, so on
	# if length of list is 5 (so up to index 4) will only do 1,2,3,4. Don't want to access sorted_list[5] (does not exist!)
	for i in xrange(1, len(sorted_list)):
		if i+1 >= len(sorted_list):
			break
		distance = abs(sorted_list[i] - sorted_list[i+1])
		if distance < smallest_distance:
			smallest_distance = distance
			start_index = i
			end_index = i+1
        

	curr_k = 2
	while curr_k < k:

		if end_index >= len(sorted_list):
			start_index -= 1
		elif start_index < 0:
			end_index +=1
		else:
			start_value = sorted_list[start_index]
			end_value = sorted_list[end_index]
			left_value = sorted_list[start_index - 1]
			right_value = sorted_list[start_index + 1]

			distance_left = abs(left_value - start_value) + abs(left_value - end_value)
			distance_right = abs(right_value - start_value) + abs(right_value - end_value)
			# There is an issue when distance_left == distance_right. We don't know which way to go!
			if distance_left < distance_right:
				start_index = start_index - 1
			elif distance_left > distance_right:
				end_index = end_index + 1
			else:
				print "h"
		
		curr_k += 1
        
	#print start_index, end_index
	sum = 0
	for i in xrange(start_index, end_index+1):
		for j in xrange(start_index, end_index+1):
			sum += (sorted_list[i] - sorted_list[j])**2
	print sum
        