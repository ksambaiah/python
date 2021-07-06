#!/usr/bin/env python3

'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
'''
class Solution:
    def findLengthOfLCIS(self, nums ) -> int:
        maxi = 0
        result = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                result += 1
            else:
                maxi = max(result, maxi)
                result = 1
        maxi = max(result, maxi)
        return maxi

if __name__ == "__main__":
    nums = [1,3,5,7]
    sol = Solution()
    print(nums)
    print(sol.findLengthOfLCIS(nums))
