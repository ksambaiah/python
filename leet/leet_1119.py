#!/usr/bin/env python3
import re
'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
'''
def sp(s):
    t = re.split('a|e|i|o|u', s)
    r = ''.join(t)
    return r


if __name__ == '__main__':
    s = "leetcodeisacommunityforcoders"
    print(s)
    print(sp(s))
