#!/usr/bin/env python3

'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
'''
def longest_substring_with_k_distinct(str1, k):
    dict1 = {}
    temp = k
    l = 0
    for x in str1:
      if temp >= 0:
         l += 1
         if x in dict1.keys():
            dict1[x] = dict1[x] + 1
         else:
            temp -= 1
            dict1[x] = 1
      else:
         if x in dict1.keys() and dict1[x] == 1:
             


if __name__ == '__main__':
   String = "araaci"
   K = 2
   print(String, K)
   print(longest_substring_with_k_distinct(String, K))
