#!/usr/bin/env python3

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

'''

def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    
    for j in range(n-1, -1, -1):
        for k in range(m+n-1-j, 0):
            if 
        
if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
   print(nums1, nums2)
   print(merge(nums1, m, nums2, n))
