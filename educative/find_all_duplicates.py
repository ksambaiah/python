#!/usr/bin/env python3

'''
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
'''
def find_duplicates(nums):
    i, l = 0, len(nums)
    duplicates= []
    while i < len(nums):
       if nums[i] != i+1:
          j = nums[i] - 1 
          if nums[i] != nums[j]:
              nums[i], nums[j] = nums[j], nums[i]
          else:
              if nums[i] not in duplicates:
                 duplicates.append(nums[i])
              i += 1
       else:
          i += 1
    return duplicates


if __name__ == '__main__':
   nums = [3,4,4,5,5,5]
   print(nums)
   print(find_duplicates(nums))
