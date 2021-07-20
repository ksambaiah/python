#!/usr/bin/env python3

'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''
def maxSubArray(a, k):
    sum = 0
    for j in range(k):
        sum  += a[j]
    sum1 = sum
    for j in range(k, len(a)):
        sum1 = sum1-a[j-k]+a[j]
        sum = max(sum, sum1)
    return sum

if __name__ == '__main__':
    a = [2, 1, 5, 1, 3, 2]
    k = 1
    print(a, k)
    print(maxSubArray(a,k))
