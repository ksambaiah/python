#!/usr/bin/env python3

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
def isValid(s) -> bool:
    b = {}
    b['('] = b['['] = b['{'] = 0
    for t in s:
       if t == '(':
          b['('] += 1
       elif t == ')':
          b['('] -= 1
       elif t == '{':
          b['{'] += 1
       elif t == '}':
          b['{'] -= 1
       elif t == '[':
          b['['] += 1
       elif t == ']':
          b['['] -= 1

    if b['('] or b['['] or b['{']:
        return False
    return True

if __name__ == '__main__':
    str = "()[]{}[]"
    print(str)
    print(isValid(str))
