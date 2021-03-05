#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:37:39 2020

@author: samkilar
"""
import sys
def binarySearch(arr, s, e, search):
    if s == e and arr[s] != search:
        return -1
    middle =  s + int( (e-s) / 2 )
    if arr[middle] == search:
        return middle
    elif arr[middle] > search:
        return binarySearch(arr, s, middle-1, search)
    else:
        return binarySearch(arr, middle+1, e, search)
       
    
    
if __name__ == "__main__":
    
    arr = [-999999, -99999, -300, -200, -100, -9, -2, -1, 0, 0, 1, 2, 9, 22, 45, 99]
    search = int(input("Please enter number: " ))
    # Got a number to search and have array, I wanted to makre sure
    # array is in ascending order and my input is with in limits
    switch = 0
    if arr[0] > arr[-1]:
        # Below is elegant way of doing reversing of array
        arr = arr[::-1]
        switch = 1

    if search < arr[0] or search > arr[-1]:
        print("Integer is not in the limits of array ")
        sys.exit(1)
    
    index = binarySearch(arr, 0, len(arr), search)
    if index == -1:
        print('Integer ',  search,  ' not found in the array')
    else:
        if ( switch == 0 ):
            print('array has index at ',  index, ' of the array')
        else:
            print('array has index at ', len(arr) - index, ' of the array')
