#!/usr/bin/env python3

'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''
def reverse(x):
    if x > 0:
       sign = 1
    else:
       sign = -1
    x = x * sign
    bignum = pow(2,31)
    y = 0
    while x:
       y = x % 10 + y * 10
       x = int(x / 10)
       if y > bignum -1:
          return 0
    y = y * sign
    return  y


if __name__ == '__main__':
    x = 123
    y = reverse(x)
    print(x)
    print(y)
