#!/usr/bin/env python3

'''
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
'''
def find_missing_number(nums):
    sum = 0 
    j = len(nums)
    for i in range(j):
        sum += nums[i]
    total = (j * (j+1)) // 2
    return (total - sum)

if __name__ == '__main__':
    arr = [0,1,5,3,4]
    print(arr)
    print(find_missing_number(arr))
