#!/usr/bin/env python3

'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''
def pair_with_targetsum(arr, target_sum):
    i, j = 0, len(arr)-1
    while j > i:
      if arr[i] + arr[j] == target_sum:
         return [i, j]
      elif arr[i] + arr[j] > target_sum:
         j -= 1
      else:
         i += 1     
    return [-1, -1]
if __name__ == '__main__':
   arr = [1, 2, 3, 4, 6]
   target = 8
   print(arr, target)
   print(pair_with_targetsum(arr, target))
