#!/usr/bin/env python3
import sys


# Fib number computation

def fibonaci(fibon):
    prev =  1
    pprev = 1
    n = 1
    print(pprev, end=" ")
    while n <= fibon:
        print(prev, end=" ")
        pprev, prev = prev, pprev + prev
        n = n + 1
    print("\n") 


if __name__  == '__main__':
   # Takes integer from the user input and prints fibonacii numbers
   fibn = int(input("Enter integer : "))
   if isinstance(fibn, int):
       fibonaci(fibn)
   else:
       print("You need to give integer number")
       sys.exit(1)
