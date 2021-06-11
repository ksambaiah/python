#!/usr/bin/env python3
import collections 

''' implementation of queue and stack using python '''

def addtostack(q, a):
    q.append(a)
    return q

def rmfromstack(q):
     return q.pop()

if __name__ == '__main__':
    # Create queue and add 3 elements
    q = collections.deque()
    q = addtostack(q, "sam")
    q = addtostack(q, "sam1")
    q = addtostack(q, "sam2")
    print(q)
    if q:
       r = rmfromstack(q)
       print(r)
    if q:
       r = rmfromstack(q)
       print(r)
    if q:
       r = rmfromstack(q)
       print(r)
    if q:
       r = rmfromstack(q)
       print(r)
