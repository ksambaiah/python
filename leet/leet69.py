#!/usr/bin/env python3

'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''
def sqri(num):
    ap = num // 2
    ep = 0.001
    while ( ( ap + num / ap ) / 2 > ep):
        ap = (ap + num / ap) / 2
        print(ap)
        if ap ** 2 <= num and (ap+1) ** 2 > num:
           print(ap)
           return int(ap)
    return int(ap)
        


if __name__ == '__main__':
   num = 1001
   print(sqri(num)) 

