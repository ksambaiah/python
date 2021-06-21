#!/usr/bin/env python3

'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''
def runningSum(nums):
    rsum = []
    sum = 0
    for x in nums:
       sum = sum + x
       rsum.append(sum)
    return rsum


if __name__ == '__main__':
    nums = [-9,1,2,3,4]
    print(nums)
    print(runningSum(nums))
