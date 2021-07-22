#!/usr/bin/env python3
import itertools

'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
'''

def find_permutation(str, pattern):
    for p in itertools.permutations(pattern):
       p = "".join(p)
       if p in str:
          return True
    return False


if __name__ == '__main__':
   str = "thisisstring"
   pattern = "ginrtsZ"
   print(str, pattern)
   print(find_permutation(str,pattern))
