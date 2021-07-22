#!/usr/bin/env python3

'''
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''
def remove_duplicates(arr):
    dup = 0
    len1 = 0
    for i in range(1,len(arr)):
        if arr[i] == arr[i-dup-1]:
           len1 += 1
           dup += 1
        else:
           dup = 0
    return len(arr)-len1
       


if __name__ == '__main__':
    arr = [2, 3, 3, 3, 6, 9, 9,9,9,9]
    print(arr)
    print(remove_duplicates(arr))
