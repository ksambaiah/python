#!/usr/bin/env python3

def reverseString(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverse = []
        index = len(s)
        while index > 0:
           reverse += s[index - 1]
           index = index - 1
        r = ''.join(reverse)
        print(r)

s = "Sambaiah1"
print(s)
reverseString(s)
