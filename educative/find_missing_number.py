#!/usr/bin/env python3

'''
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
'''
def find_missing_number(nums):
    
    i, n = 0, len(nums) 
    while i < len(nums):
       j = nums[i] 
       if nums[i] < n and nums[i] != i:
          nums[i], nums[j] = nums[j], nums[i] 
       else:
          i += 1
    for i in range(n):
       if nums[i] != i:
          return i
    

if __name__ == '__main__':
    arr = [0,1,5,3,2]
    print(arr)
    print(find_missing_number(arr))
