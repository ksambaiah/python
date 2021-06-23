#!/usr/bin/env python3

def removeElement(nums, val):
    s = set(nums)
    t = set([val])
    print(s.difference(t))
    return len(s.difference(t))

if __name__ == '__main__':
    nums = [1,2,3,4,5,5,3]
    val = 5
    print(nums,val)
    print(removeElement(nums,val))
