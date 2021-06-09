#!/usr/bin/env python3
from typing import Dict
'''
  Eventhough it is easy program I am writing it to see what -> in
  function definition.
  $author$
'''

def fib2(n: int) -> int:
    if n not in memo:
       memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]
  
if __name__ ==  "__main__":
    memo: Dict[int, int] = {0: 0, 1: 1}
    print(fib2(99))
