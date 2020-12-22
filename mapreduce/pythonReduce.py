#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:26:25 2020

@author: samkilar
"""
import functools

# map Reduce examples
def sumArray(lis):
    
    return functools.reduce(lambda a,b : a+b,lis)

  
if __name__ == "__main__":
    # We are taking array, later we do take some random values
    arr = [0, 1, -100, -200, 300, 999999, 9, 99, 0, 2, 22, 45, -9, 99999]
    print("Sum of array is ", sumArray(arr))