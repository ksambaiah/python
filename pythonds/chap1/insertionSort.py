#!/usr/bin/env python3
import random

''' This is sorting algorithm for insertion Sort '''

def insertSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0  and a[j] > key:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key 
    return a

if __name__ == '__main__':
    # Generate random integers around 1000
    a = []
    for i in range(1000):
        a.append(random.randrange(-9999999, 9999999))
    print(a)
    a = insertSort(a)
    print(a)
    for i in range(1000):
        k = random.randrange(0,1000)
        l = random.randrange(k,1000)
        if a[k] > a[l]:
            print("sorting is not right")
        else:
            print("good")

