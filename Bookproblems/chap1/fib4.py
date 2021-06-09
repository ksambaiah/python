#!/usr/bin/env python3

'''  This example uses lru_cache This function uses memorisation
of functions 
Ideally this function should take longer time, but lru_cache does
the trick.

'''


from functools import lru_cache
@lru_cache(maxsize=None)

def fib(n: int) -> int: 
    if n < 2: # base case
        return n
    return fib(n - 2) + fib(n - 1) 

if __name__ == "__main__":
    print(fib(5))
    print(fib(50))
