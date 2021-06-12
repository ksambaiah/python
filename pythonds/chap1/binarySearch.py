#!/usr/bin/env python3
import random

def binarySearch(a, left, right, num):
    if  right >= left:
         middle =  (right + left) // 2
         if a[ middle ] == num:
             return middle
         elif a [ middle ] > num:
             return binarySearch(a, left, middle-1, num) 
         else:
             return binarySearch(a, middle+1, right, num)
    else:
         return -1

if __name__ == '__main__':
    size = 2000
    a = []
    
    for i in range(0,size):
        if i != 0: 
           num = a[i-1]
           a.append(random.randint(num, num+5000))
        else:
           a.append(0)
    m = a[220]
    print(m)
    match = binarySearch(a,0,len(a), m)
    print(match)
