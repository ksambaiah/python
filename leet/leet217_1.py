#!/usr/bin/env python3

def containsDuplicate(nums) -> bool:
        b = set(nums)
        if len(b) == len(nums):
           return False
        else:
           return True

if __name__ == '__main__':
   a = [1,2,3,4,1]
   print(a)
   print(containsDuplicate(a))
