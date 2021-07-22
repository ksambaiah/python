#!/usr/bin/env python3
import itertools
'''
Permutations of a string
abc
abc, acb, bac, bca, cab, cba
'''

if __name__ == '__main__':
    str = "abc"
    print(str)
    for p in itertools.permutations(str):
        p = "".join(p)
        print(p)
