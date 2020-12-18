#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:32:54 2020

@author: samkilar
"""
import random

def selection_sort(a):
    for i in range(0, len(a)):
        # Assume a[i] is minimal and i is index
        mindex = i
        for j in range(i+1, len(a)):
            if a[j] < a[mindex]:
                mindex = j
        # if i is minimal no need of exchange.
        a[i], a[mindex] = a[mindex], a[i]
    return a


if __name__ == "__main__":
    # Generate random integer. it has to be positive
    index = random.randint(1, 99)
    print(index)
    arr = []
    ## Generate Random elements
    for i in range(0, index):
        arr.append(random.randrange(-99999999, 99999999))
    print("Array before sorting")
    print(arr)
    arr = selection_sort(arr)
    print("Array after sort")
    print(arr)