#!/usr/bin/env python3
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
def missingNumber(nums):
    return int((len(nums) * len(nums)+1) / 2 - sum(nums))


if __name__ == '__main__':
   nums = [9,6,4,2,3,5,7,0,1]
   print(nums)
   print(missingNumber(nums))
