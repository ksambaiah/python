#!/usr/bin/env python3
'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''
def degreeArray(a):
    deg = {}
    dis = {}
    for i in range(len(a)):
       if a[i] in deg.keys():
          deg[a[i]] = 1 + deg[a[i]]
          dis[a[i]] = i - dis[a[i]] 
       else:
          deg[a[i]] = 1
          dis[a[i]] = i
    max = 0
    a = []
    for i in deg.keys():
        if deg[i] >= max:

if __name__ == '__main__':
    a = [1,1,2,2,2,1,3,4,5]
    print(a)
    print(degreeArray(a))
