#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:51:09 2020

@author: samkilar
"""

def quicksort(a):
    if len(a) <= 1:
        return a
    
    # Functional style calling lessa and greata recursively
    lessa = [x for x in a[1:] if x <= a[0]]
    greata = [x for x in a if x > a[0]]
    return quicksort(lessa) + [a[0]] + quicksort(greata)
    
    
if __name__ == "__main__":
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, -300, -999999, 9, 99, 0, 2, 22, 45, -9, -99999]
    print("Array before sorting")
    print(arr)
    qarr = quicksort(arr)
    #arr = quicksort(arr)
    #print("Array after sort")
    print(qarr)
