#!/usr/bin/env python3

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
def singleNumber(nums):
    result = 0;
    for i in nums:
        result ^= i
        print(result)
    return result
       


if __name__ == '__main__':
    a = [4,1,3,1,2,2,3,4,5]
    print(a)
    print(singleNumber(a))
