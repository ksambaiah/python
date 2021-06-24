#!/usr/bin/env python3

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

def isAnagram(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)
    return s == t

if __name__ == "__main__":
    s = "Sambaiah"
    t = "ambaiahS"
    print(s,t)
    print(isAnagram(s,t))
