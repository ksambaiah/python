#!/usr/bin/env python3

def gcd(a: int, b: int) ->  int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
     a = 64
     b = 16
     if b <= a:
        r = gcd(a,b)
     else:
        r = gcd(b,a)
     print(a,b,r)
