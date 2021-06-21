#!/usr/bin/env python3

'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
'''
def signOf(x):
    y = [a  for a in x if a < 0]
    z = [a  for a in x if a > 0]
    if (len(y) + len(z)) < len(x):
       return 0
    if len(y) % 2:
       return -1
    return 1




if __name__ == '__main__':
    x = [-1,2,3,4,5,6,7]
    print(signOf(x))
    x = [-1,0,2,3,4,5,6,7]
    print(signOf(x))
