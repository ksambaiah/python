#!/usr/bin/env python3

from functools import lru_cache


'''
  Eventhough it is easy program I am writing it to see what -> in
  function definition.
  $author$
  I like this most, next examples use some special functions.
'''

def fib3(n: int) -> int:
    if n < 2:
       return n
    return fib3(n-1) + fib3(n-2)
  
if __name__ ==  '__main__':
    @lru_cache(maxsize=None)
    print(fib3(99))
