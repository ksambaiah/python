#!/usr/bin/env python3

'''
Given two binary strings a and b, return their sum as a binary string.
'''

def addBinary(a: str, b: str):
    zero = "0"
    if len(a) < len(b):
       a =  (zero * (len(b)-len(a))) + a 
    else:
       b =  (zero * (len(a)-len(b))) + b 
    carry = 0
    c = ""
    for i in range(-1,-len(a)-1,-1):
       t = int((int(b[i]) + int(a[i]) + carry) % 2)
       carry = (int(b[i]) + int(a[i]) + carry) // 2
       c = str(t) + c
       i -= 1
    if  carry :
       c = str(carry) + c
 
    return c
if __name__ == '__main__':
   a = "1010"
   b = "1011"
   print(a,b)
   print(addBinary(a,b))
