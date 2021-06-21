#!/usr/bin/env python3

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
def isValid(s) -> bool:
    if len(s) % 2:
            return False
    i = 0
    while i < len(s):
        if s[i] == '(':
            if s[i+1] == ')':
               i = i+ 2
            else:
               return False
        elif s[i] == '{':
            if s[i+1] == '}':
                i = i+ 2
            else:
                return False
        elif s[i] == '[':
            if s[i+1] == ']':
               i = i+ 2
            else:
                return False
        else:
                return False
    return True
        


if __name__ == '__main__':
    str = "{[]}"
    print(str)
    print(isValid(str))
