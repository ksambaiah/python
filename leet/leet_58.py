#!/usr/bin/env python3

'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
'''

def lengthOfLastWord(s: str):
    r = s.split(" ")
    for j in range(-1, -len(r)-1, -1):
       if len(r[j]) > 0:
          return len(r[j])
    return 0


if __name__ == '__main__':
#s = "Hello, world s"
   s =  "a     "
   print(s)
   print(lengthOfLastWord(s))
