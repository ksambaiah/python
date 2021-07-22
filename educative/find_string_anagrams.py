#!/usr/bin/env python3
import itertools

'''
'''

def find_string_anagrams(str, pattern):
    arr = []
    for p in itertools.permutations(pattern):
       p = "".join(p)
       #arr.append(str.find(p))
       if p in str:
          arr.append(str.index(p))
    arr.sort()
    return arr


if __name__ == '__main__':
   str = "thitrisisstringirtritrti"
   pattern = "tri"
   print(str, pattern)
   print(find_string_anagrams(str,pattern))
