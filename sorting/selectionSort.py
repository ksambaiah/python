#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:29:17 2020

@author: samkilar
"""

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
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, -300, 9, 99, 0, 2, 22, 45, -9, -99999]
    print("Array before sorting")
    print(arr)
    arr = selection_sort(arr)
    print("Array after sort")
    print(arr)