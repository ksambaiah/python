#!/usr/bin/env python3

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''
def maxSubArray(nums):
    max1 = curr = nums[0]
    for i in range(1,len(nums)):
        curr = max(nums[i], curr + nums[i])
        max1 = max(max1, curr)
    return max1

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(nums)
    print(maxSubArray(nums))
