#!/usr/bin/env python3

'''
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):

        missing = []
        nums.insert(0, lower-1)
        nums.append(upper+1)
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
               missing.append(str(nums[i]-1))
            elif nums[i] - nums[i-1] > 2:
               m = str(nums[i-1]+1) + "->" + str(nums[i]-1)
               missing.append(m)
        return missing


if __name__ == '__main__':
    nums = [-1,0,1,3,50,75]
    lower = 0
    upper = 99
    print(nums, lower, upper)
    sol = Solution()
    print(sol.findMissingRanges(nums, lower, upper))

