#!/usr/bin/env python3

''' Remove duplicates from array '''

def removeDup(a):
    k = 0
    j = 1
    while j < len(a):
        if a[j] != a[j-1]:
            k += 1
            a[k] = a[j]
        j += 1
    return a[:k+1] 
if __name__ == '__main__':

    arr = [0,0,1,1,1,1,1,4,4,5,6,7,8,9,10,11,11,11,12,13,13,13,14,14,14]
    print(arr)
    arr = removeDup(arr)
    print(arr)
