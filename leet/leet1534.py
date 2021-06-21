#!/usr/bin/env python3
'''
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
'''
def goodArray(arr,a,b,c):
    result = 0
    l = len(arr)
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
               a1 = abs(arr[j] - arr[i]) <= a
               b1 = abs(arr[j] - arr[k]) <= b
               c1 = abs(arr[k] - arr[i]) <= c
               if a1 and b1 and c1:
                    result += 1
    return result


if __name__ == '__main__':
   arr = [3,0,1,1,9,7]
   a = 7
   b = 2
   c = 3
   print(arr,a,b,c)
   print(goodArray(arr,a,b,c))
