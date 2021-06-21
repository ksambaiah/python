#!/usr/bin/env python3

'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
'''
def arraysIntersection(arr1, arr2, arr3):
    newA = []
    j = 0
    for i in range(len(arr1)):
        while arr1[i] < arr2[j] and i < len(arr1):
            i += 1
        while (arr2[j] < arr1[i]) and j < len(arr2):
            j += 1
        if  arr1[i] == arr2[j] and i < len(arr1) and j < len(arr2):
            newA.append(arr1[i])
            if i == len(arr1) - 1 or j == len(arr2) - 1:
                  break
            i += 1
            j += 1
    return newA        

if __name__ == '__main__':
     arr1 = [1,2,3,4,5]
     arr2 = [1,2,5,7,9]
     arr3 = [1,3,4,5,8]
     print(arr1, arr2, arr2)
     print(arraysIntersection(arr1, arr2, arr3))
