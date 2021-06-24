#!/usr/bin/env python3

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
def isValid(s) -> bool:
    if len(s) % 2:
            return False
    dict = {"(": ")", "[": "]", "{": "}"}
    for i in range(0, len(s)-1, 2):
        if s[i] not in dict.keys():
             return False
        if dict[s[i]] != s[i+1]:
             return False
    return True


if __name__ == '__main__':
    str = "{}[]{]"
    print(str)
    print(isValid(str))
