#!/usr/bin/evn python3

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''
def inter(nums1, nums2):
    return (set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
   nums1 = [1,2,2,1]
   nums2 = [2,2]
   print(nums1)
   print(nums2)
   print(inter(nums1,nums2))
