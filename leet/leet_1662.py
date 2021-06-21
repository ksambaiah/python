#!/usr/bin/env python3

'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''
def compare(x,y):
    u = "".join(x)
    v = "".join(y)
    print(u)
    print(v)
    return u == v


if __name__ == '__main__':
    x = ["ab", "c"]
    y = ["ab", "bc"]
    print(compare(x,y))
