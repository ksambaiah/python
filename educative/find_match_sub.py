#!/usr/bin/env python3

'''
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 12, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
'''
def smallest_subarray_with_given_sum(s, arr):
    l = 0 
    found = 0
    sum  = 0
    maxi = len(arr)
    for i in range(len(arr)):
        sum  += arr[i]
        l  += 1
        while sum >= s and l >= 1:
           maxi = min(maxi, l)
           sum = sum - arr[i+1-l]
           found = 1
           if l == 1:
              return l
           l -= 1
    if not found:
       return 0
    return maxi
            
if __name__ == '__main__':
   arr = [234, 1, 5000, 2, 13, 122]
   s = 2350
   print(s,arr)
   print(smallest_subarray_with_given_sum(s,arr))
