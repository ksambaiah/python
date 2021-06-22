#!/usr/bin/env python3
import sys

'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
'''
def maxSubseq(arr,k):
    maxi = -(sys.maxsize)-1
    for i in range(len(arr)-k+1):
        sum = 0
        for j in range(i, i+k):
           sum += arr[j]
        maxi = max(maxi,sum)
         
    return maxi


if __name__ == '__main__':
    arr = [2,1,5,1,3,2] 
    k  = 3
    print(arr,k)
    print(maxSubseq(arr,k))
