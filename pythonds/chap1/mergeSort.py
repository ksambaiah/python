#!/usr/bin/env python3
import random

'''
   Merge Sort of python
'''
def mergesort(a, 


if __name__ == '__main__':
    size = 1000
    a = []
    for i in range(size):
        a.append(random.randint(-999999,9999999))
    a = mergesort(a, 0, len(a))
    
