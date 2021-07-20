#!/usr/bin/env python3

'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        arr = []
        for x in nums1:
            found = 0
            for j in range(len(nums2)):
                if x == nums2[j]:
                    found = 1
                elif found and x < nums2[j]:
                    arr.append(nums2[j])
                    break
                if j == len(nums2) - 1:
                    arr.append(-1)
        return arr

if __name__ == '__main__':
   nums1 = [2,4]
   nums2 = [1,2,3,4]
   print(nums1, nums2)
   s = Solution()
   print(s.nextGreaterElement(nums1, nums2))
