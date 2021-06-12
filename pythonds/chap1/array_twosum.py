#!/usr/bin/env python3

''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
def arrayTwo(arr, sum):
    size = len(arr)
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i] + arr[j] == sum:
                return i,j 
    return 0,0

if __name__ == '__main__':
    arr = [1,4,7,9,12,14,16,19]
    sum = 19
    ind1, ind2 = arrayTwo(arr, sum)
    if ind1 == 0 and ind2 == 0:
        print("No indices matched")
    else:
        print("arr, sum", arr, sum)
        print("matched indices are", ind1, ind2)
