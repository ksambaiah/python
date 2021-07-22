#!/usr/bin/env python3

'''
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''
def fruits_into_baskets(fruits):
    dict = {}
    length = 0
    maxi = 0
    for i in range(len(fruits)):
      if fruits[i] in dict:
         dict[fruits[i]] += 1
         length += 1
         maxi = max(maxi, length)
      elif fruits[i] not in dict and len(dict.keys()) < 2:
         dict[fruits[i]] = 1
         length += 1
         maxi = max(maxi, length)
      elif fruits[i] not in dict and len(dict.keys()) == 2:
          maxi = max(maxi, length)
          while len(dict.keys()) == 2:
             if dict[fruits[i-length]] == 1: 
                del dict[fruits[i-length]]
                length -= 1
             else:
                dict[fruits[i-length]] -= 1
                length -= 1
          dict[fruits[i]] = 1
          length += 1
    return maxi
if __name__ == '__main__':
   fruits=['A', 'B', 'A', 'C', 'A', 'C', 'C', 'A', 'A', 'D']
   print(fruits)
   print(fruits_into_baskets(fruits))
