#!/usr/bin/env python3

'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''

def mySqrt(x: int) -> int:
    y =  x / 2
    epsilon = 0.05
    while abs( x - y ** 2) > epsilon:
        y = ( y + x/y) / 2
       
    print(y)
    return int(y)



if __name__ == '__main__':
   x = 29
   print(x)
   print(mySqrt(x))
