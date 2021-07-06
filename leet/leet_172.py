#!/usr/bin/env python3

'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
         result = 0
         while n > 0:
            result += n // 5
            n = n // 5
         return result

if __name__ == "__main__":
    n = 30
    print(n)
    sol = Solution()
    print(sol.trailingZeroes(n))
