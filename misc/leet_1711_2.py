#!/usr/bin/env python3
'''
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.
'''
def countPairs(a):
     mapped = {}
     cnt = 0
     for n in deliciousness:
         if n in mapped:
            cnt += mapped[n]
            for i in range(22):
                rem = 2**i - n
                if rem in mapped:
                    mapped[rem] += 1
                else:
                    mapped[rem] = 1
        return cnt % (10**9 + 7)


if __name__ == '__main__':
   #a = [1,3,5,7,9]
   a = [1,1,1,3,3,3,7]
   print(a)
   print(countPairs(a))
