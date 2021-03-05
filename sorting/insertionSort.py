#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 03:00:16 2020

@author: samkilar
"""

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        temp = arr[i]
        while( temp < arr[j-1] and j > 0):
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    return arr


if __name__ == "__main__":
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, -300, -999999, 9, 99, 0, 2, 22, 45, -9, -99999]
    print("Array before sorting")
    print(arr)
    arr = insertionSort(arr)
    print("Array after sort")
    print(arr)
            
            
