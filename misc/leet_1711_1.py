#!/usr/bin/env python3
'''
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.
'''
def countPairs(a):
    sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
          n = a[i] + a[j]
          if  (n & (n-1) == 0) and n != 0:
              sum  += 1
    return sum


if __name__ == '__main__':
   #a = [1,3,5,7,9]
   a = [1,1,1,3,3,3,7]
   print(a)
   print(countPairs(a))
