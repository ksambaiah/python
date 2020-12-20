#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:52:18 2020

@author: samkilar
"""

"""
This program takes array and number less than len(array) and rotates
[0,1,2,3,4,5,6,7,8,9] and given 5 it rotates
[5,6,7,8,8,0,1,2,3,4]
or given 3
[3,4,5,6,7,8,9,0,1,2]
"""
def rotateArray(arr, r):
    #arr[3::-1] first 3 elements reveresed
    #arr[:-7:-1] last 7 elements reversed
    # a[::-1] is reverse
    # Best explanantion is hand waving for this algorithm
    arr = arr[r-1::-1] + arr[:-(len(arr)-r+1):-1]
    return(arr[::-1])
     

if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8,9] 
    print(arr)
    r = 4
    if r > len(arr):
        arr = arr
    else:
        arr = rotateArray(arr, r)
    print(arr)
