#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 00:41:04 2020

@author: samkilar
"""

def addArray(arr):
    y = 0
    for i in range(len(arr)):
        y = y + arr[i]
        
    return y

if __name__ == "__main__":
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, 300, 999999, 9, 99, 0, 2, 22, 45, -9, 99999]
    print("Adding all emements of array", addArray(arr))