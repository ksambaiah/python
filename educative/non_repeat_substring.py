#!/usr/bin/env python3

'''
Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
'''
def non_repeat_substring(str1):
    dict1 = {}
    length = 0
    maxi = 1
    for i in range(len(str1)):
        if str1[i] in dict1:
           dict1 = {}
           length = 1
           dict1[str1[i]] = 1
        else:
           length  += 1
           dict1[str1[i]] = 1
           maxi = max(maxi, length)
    return maxi 

if __name__ == '__main__':
    str1 = "aaaaaaaa"
    print(str1)
    print(non_repeat_substring(str1)) 
