#!/usr/bin/env python3
from functools import reduce
from math import gcd

'''
Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.
'''
def gcdmultip(a):
     return reduce(gcd, a) == 1    
if __name__ == '__main__':
    a = [30,6,9,18,22,34,42,55,66]
    print(a)
    print(gcdmultip(a))
