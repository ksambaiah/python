#!/usr/bin/env python3

'''
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
'''

def make_squares(arr):
  for i in range(len(arr)):
      if arr[i] == 0:
         break
  if i == len(arr) - 1:
      arr = arr[::-1]
      i = 0
  if i == 0:
      sqares = [x ** 2 for x in arr]
      return squares
  arr = [abs(x) for x in arr]
  j = i - 1 
  k = i + 1
  count = 0
  while j >= 0 or k < len(arr):
     if a[j] <= a[k]:
        count += 1
        j  -= 1
     else:
if __name__ == '__main__':
   arr =  [-2, -1, 0, 2, 3]
   print(arr)
   print(make_squares(arr))
