#!/usr/bin/env python3

'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

def plusOne(digits):

    for j in range(len(digits)-1, -1, -1):
        if digits[j] != 9:
           digits[j] += 1
           return digits
        else:
           digits[j] = 0
    digits.insert(0,1)
    print(digits)
if __name__ == '__main__':
   a = [9,9,9]
   print(a)
   print(plusOne(a))
