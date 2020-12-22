#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:30:00 2020

@author: samkilar
"""


# map Reduce examples
def addToArray(lis):
    
    return list(map((lambda a : a+2),lis))

  
if __name__ == "__main__":
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, -300, 999999, 9, 99, 0, 2, 22, 45, -9, 99999]
    arr1 = addToArray(arr)
    print("Adding 2 to the array", arr1)