#!/usr/bin/env python3

''' Given key, finding minimum number of elements in array equal to key or greater
than key '''

def slidingWindow1(arr, num):
    total  = 0
    found = 0
    elem = 0
    sum = 0
    for i in range(len(arr)):
       sum = sum + arr[i]
       total = total + 1
       print(sum, total)
       if sum >= num:
           if found  == 0:
              found = 1
              elem = total
           else:
              if total < elem:
                 elem = total
           total =  0
    return elem

if __name__ == '__main__':

   arr = [10, 20, 30, -40, 50, 6, 7, 4, 44, 99, 12, 123, 145]
   key = 7799999999
   r = slidingWindow1(arr, key)
   print(arr)
   print("Number of arrary elements are  ", r)
