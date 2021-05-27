#!/usr/bin/env python3

'''
  Eventhough it is easy program I am writing it to see what -> in
  function definition.
  $author$
'''

def fib1(n: int) -> int:
    if n == 1 or n == 0:
       return 1 
    return fib1(n - 1) + fib1(n -2)

  
if __name__ ==  "__main__":
    print(fib1(5))
