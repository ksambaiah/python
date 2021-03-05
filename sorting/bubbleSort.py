#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:20:00 2020

@author: samkilar
"""

def bubbleSort(arr):
    for i in range(len(arr)):
    # Like bubble largest element comes to last in array.
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, -300, 9, 99, 0, 2, 22, 45, -9, -99999]
    print("Array before sorting")
    print(arr)
    arr = bubbleSort(arr)
    print("Array after sort")
    print(arr)
