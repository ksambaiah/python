#!/usr/bin/env python3

'''
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
'''
def find_duplicate(nums):
    i, l = 0, len(nums)
    while i < len(nums):
       j = nums[i] - 1
       if nums[i] != i+1 and nums[i] != nums[j]:
          nums[i], nums[j] = nums[j], nums[i]
       elif nums[i] == nums[j] and i != j:
          return nums[i]
       else:
          i += 1


if __name__ == '__main__':
   nums = [1, 5, 2, 3, 2]
   print(nums)
   print(find_duplicate(nums))
