#!/usr/bin/env python3

def containsDuplicate(nums) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
               print(nums[i], nums[j])
               if nums[i] == nums[j]:
                  return True
        return False

if __name__ == '__main__':
   a = [1,2,3,4]
   print(a)
   print(containsDuplicate(a))
