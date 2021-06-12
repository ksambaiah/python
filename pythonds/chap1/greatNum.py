#!/usr/bin/env python3

''' leet 1431
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
'''
def greatNum(arr, num) -> List[bool]:
    max = arr[0]
    b = []
    for i in range(1,len(arr)):
        if max < arr[i]:
           max = arr[i]
    for i in range(len(arr)):
        if arr[i] + num >= max:
           b.append(True)
        else:
           b.append(False)
    return b

if __name__ == '__main__':
   arr = [1,3,4,7,8,9,1,2,3,4,5]
   extra = 6
   print(arr,extra)
   ret = greatNum(arr,extra)
   print(ret)
