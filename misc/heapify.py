#!/usr/bin/env python3

''' This is heapify function, given array we create heap '''

def heapify(a,i):
    l = 2 * i + 1
    r = 2 * i + 2
    larr = len(a) - 1
    largest = i
    if l <= larr and a[l] > a[largest]:
        largest = l
    if r <= larr and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest)
    return a

def buildheap(a):
     size = len(a) // 2 
     for i in range(size, -1, -1):
          a = heapify(a,i)
     return a

if __name__ == '__main__':
    arr = [10, 5, -6, 7, 0, 9, 91, 21, 12, 13, 4]
    print(arr)
    arr1 = buildheap(arr)
    print(arr1)
    
