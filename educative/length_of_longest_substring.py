#!/usr/bin/env python3

'''
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
'''

def length_of_longest_substring(str, k):
    maxi = 0
    for i in range(len(str)):
       dict1 = {}
       dict1[str[i]] = 1
       length = 1
       found = 1
       for j in range(i+1, len(str)):
          if str[j] in dict1:
             length += 1 
          elif found:
             dict1[str[j]] = 1
             found = 0
             length += 1 
          elif found == 0:
             maxi = max(maxi, length)
             break
       if j == len(str)-1:
           maxi = max(maxi, length)
           return maxi
    return maxi

if __name__ == '__main__':
   str = "abbcb"
   k = 1
   print(str, k)
   print(length_of_longest_substring(str, k))
