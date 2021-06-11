#!/usr/bin/env python3

# Given a number find no. of bits set to 1

def numBits(x):
    numBitsf = 0
    while x :
       numBitsf +=  x & 1
       x >>= 1
    return numBitsf


if __name__ == '__main__':
    x = 1024
    b = numBits(x)
    print("For number {0} no. of bits are {1}".format(x,b))
