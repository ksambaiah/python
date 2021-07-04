#!/usr/bin/env python3

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
def isValid(s):
    dict = {"{": "}", "[": "]", "(": ")"}
    ar = []
    for x in s:
        print(ar)
        if x in dict:
           ar.append(x)
        elif len(ar) == 0 or dict[ar.pop()] != x:
           return False
    return len(ar) == 0

if __name__ == '__main__':
   s = "()"
   print(s)
   print(isValid(s))
