#!/usr/bin/env python3

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while  left <= right:
        mid = left + int( (right - left) / 2)
        if nums[mid] >= target:
           right = mid - 1
        else:
           left =  mid + 1
    return left
    

if __name__ == "__main__":
   nums = [1,3,5,6]
   target = 5
   print(nums,target)
   print(searchInsert(nums,target))
