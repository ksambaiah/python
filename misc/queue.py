#!/usr/bin/env python3
import collections 

''' implementation of queue and stack using python '''

def addtoQueue(q, a):
    q.append(a)
    return q

def rmfromQueue(q):
     return q.popleft()

if __name__ == '__main__':
    # Create queue and add 3 elements
    q = collections.deque()
    q = addtoQueue(q, "sam")
    q = addtoQueue(q, "sam1")
    q = addtoQueue(q, "sam2")
    print(q)
    if q:
       r = rmfromQueue(q)
       print(r)
    if q:
       r = rmfromQueue(q)
       print(r)
    if q:
       r = rmfromQueue(q)
       print(r)
    if q:
       r = rmfromQueue(q)
       print(r)
