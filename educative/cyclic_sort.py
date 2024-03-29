#!/usr/bin/env python3

'''
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
'''
def cyclic_sort(nums):
    
    i = 0
    while i < len(nums):
       j = nums[i] - 1
       if nums[i] == i+1:
          i += 1
       else:
          nums[i], nums[j] = nums[j], nums[i] 
    
    return nums

if __name__ == '__main__':
    arr = [3,1,5,4,2]
    print(arr)
    print(cyclic_sort(arr))
