#!/usr/bin/env python3
import sys
#  Maximum sum of contiguous array of size 3
# Not sure how to get minint getting maxint and negating

def slidingWindow2(arr, num):
    total = 0
    ptotal = 0
    for i in range(len(arr)):
        if i < num:
           total = total + arr[i]
           ptotal = total
        else:
           total = total + arr[i] - arr[i-num]
           if ptotal < total: 
              ptotal = total 
              print(total,arr[i],arr[i-num])
              
            
    return ptotal

if __name__ == '__main__':

   arr = [-10000, 20, 30, -40, 50, 6, 7, 4, 44, 99, 12, 123, -145, 20000000000]
   key = 3
   r = slidingWindow2(arr, key)
   print(arr)
   print("maximum of 3 adjucent numbers are   ", r)
