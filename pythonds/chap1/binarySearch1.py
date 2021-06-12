#!/usr/bin/env python3
import random

''' 
  binary search practice 

'''
def binarySearch(a,left,right,key):
    if right >= left:
       middle = left + (right - left) // 2
       if a[middle] == key:
          return middle
       elif a[middle] < key:
          return binarySearch(a, middle+1, right, key)
       else:
          return binarySearch(a, left, middle-1, key)
    else:
       return -1 


if __name__ == '__main__':
    size = 5000
    a = []
    a.append(2)
    
    for i in range(1,size):
       a.append(random.randint(a[i-1], a[i-1]+500))
    key = a[25]
    s = binarySearch(a,0,len(a),key)
    print(s)
