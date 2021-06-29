#!/usr/bin/env python3

'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
'''
def removeElement(nums, val):
    k = 0
    for i in range(0,len(nums)):
        if nums[i] == val:
           k = k + 1
        else:
            nums[i-k] = nums[i]
    for j in range(len(nums)-k,len(nums)):
        nums[j] = 0
    print(nums)
    print(k)
    return len(nums)-k
if __name__ == '__main__':
#    a = [0,1,1,1,2,2,3,3,4,4,4,4,4,4,4,5,5]
    a = [3,2,2,3]
    print(a)
    l = 3
    print(removeElement(a,l))
