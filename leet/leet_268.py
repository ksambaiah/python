#!/usr/bin/env python3
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
def missingNumber(nums):
    l = [x for  x in range(len(nums)+1) ]
    return list((set(l)).difference(set(nums)))
    eturn list((set(s)).difference(set(nums)))


if __name__ == '__main__':
   nums = [9,6,4,2,3,5,7,0,1]
   print(nums)
   print(missingNumber(nums))
