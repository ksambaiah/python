#!/usr/bin/env python3
'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''
def goodPairs(a):
    b = {}
    for x in a:
       if x in b: 
          b[x] += 1
       else:
          b[x] = 1
    sum = 0
    for key in b.keys():
        print(b[key])
        sum = sum + int (b[key] * (b[key]-1)) // 2
    return sum

if __name__ == '__main__':
     a = [1,1,1,1,1,1]
     print(a)
     print(goodPairs(a))
