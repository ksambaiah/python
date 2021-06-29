#!/usr/bin/env python3

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
def searchInsert(nums,target):
    r = len(nums)
    l = 0
    mid = (r -l )  // 2
    seen = 0
    p = mid
    while True:
        print(mid)
        if nums[mid] > target:
           print(seen)
           if seen:
              return p
           l = mid + 1
           mid = mid + ( r - l ) // 2
        elif nums[mid] <  target:
           if seen:
              return p
           r = mid-1
           mid = ( r - l ) // 2
        else:
           if r - l  == 1:
              return mid
           seen = 1
           r = mid - 1
           p = r
           mid = ( r - l ) // 2
        
if __name__ == '__main__':
    nums = [1,2,3,5,5,5]
    target = 5
    print(nums,target)
    print(searchInsert(nums,target))
