#!/usr/bin/env python3

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

'''

def merge(nums1, m: int, nums2, n: int):
    last, i, j = m+n-1, m-1, n-1
    
    while i >= 0 and j >= 0:
       if nums1[i] > nums2[j]:
          nums1[last] = nums1[i]
          i, last = i-1, last - 1
       else:
          nums1[last] = nums2[j]
          j, last = j-1, last-1

    print(nums1)
    while j >= 0:
       nums1[last] = nums2[j]
       j, last = j-1, last-1
    return nums1
     
if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2 = [5]
    n = 1
    print(nums1, nums2)
    print(merge(nums1, m, nums2, n))
