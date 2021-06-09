#!/usr/bin/env python3

def reverseString(s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l // 2):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        print(s)

s = ["S", "a", "m", "b", "a", "i", "a", "h"]
print(s)
reverseString(s)
s = ["S", "a", "m", "b", "a", "i", "a", "h", "k"]
print(s)
reverseString(s)
