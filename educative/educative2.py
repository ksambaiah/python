#!/usr/bin/env python3
import sys

'''
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
'''
def maxSubseq(arr,k):
    maxS  = len(arr) + 100
    for i in range(len(arr)):
        window_sum = 0
        j = i
        while window_sum < k and j < len(arr):
           window_sum += arr[j]
           j += 1
        if window_sum >= k: 
           maxS = min(maxS, j - i )
    return maxS


if __name__ == '__main__':
    arr = [2,1,5,1,3,2] 
    k  = 7
    print(arr,k)
    print(maxSubseq(arr,k))
