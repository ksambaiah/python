#!/usr/bin/env python3

''' This is intresting merge useful in merge sort '''

def merge(a, p, q, n):
    r = q+1
    for i in range(p,n):
        if r <= n and a[r] < a[i]:
           pivot = a[r]
           for j in range(r,i,-1):
               a[j] = a[j-1]          
           a[i] = pivot
           r = r+1
    return a
           

if __name__ == '__main__':
    a = [-20,1,2,3,4,5,900,-2000,-204,9,20,21,222,222]
    print(a)
    a = merge(a, 0, 6, 13)
    print(a)
