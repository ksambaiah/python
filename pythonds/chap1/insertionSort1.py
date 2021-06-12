#!/usr/bin/env python3
import random

''' insertion sort again to see how it improved my learnings '''

def insertSort(a):
    for i in range(1, len(a)):
        pivot = a[i]
        j = i-1
        while j >= 0 and a[j] > pivot:
             a[j+1] = a[j]
             j = j - 1
        a[j+1] = pivot
    return a


if __name__ == '__main__':

    size = random.randint(50000,50000199)
    print(size)
    arr = []
    for i in range(size):
        arr.append(random.randint(-9000000, 99999999))
    arr = insertSort(arr)
    for i in range(2):
        j = random.randint(0,len(arr)-1)
        k = random.randint(j,len(arr)-1)   
        print(j,k)
        if arr[j] > arr[k]:
           print("Sorting is not right")

