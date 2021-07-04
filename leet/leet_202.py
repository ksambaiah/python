#!/usr/bin/env python3

'''
Write an algorithm to determine if a number n is happy.
'''

def getSquares(m):
    sum = 0
    while m:
       sum += ( m % 10 ) ** 2
       m = m // 10
    return sum

def isHappy(n: int) -> bool:
    seen = []
    for i in range(100):
        n = getSquares(n)
        if n == 1:
           return True
        if n in seen:
           return False
        else:
           print(n)
           seen.append(n)
    return False

if __name__ == '__main__':
   n = 2222222
   print(n)
   print(isHappy(n))
