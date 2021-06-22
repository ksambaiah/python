#!/usr/bin/env python3

'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.
'''

def longest_substring_with_k_distinct(str1, k):
    len = 0
    for x in str1:
       print(x)
    return 1

if __name__ == '__main__':
    String="araaci"
    K=2
    print(String,K)
    print(longest_substring_with_k_distinct(String,K))
