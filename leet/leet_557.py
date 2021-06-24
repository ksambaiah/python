#!/usr/bin/env python3

'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

def reverseWords(s: str):
   t = s.split(" ")
   for i in range(len(t)):
      x = t[i]
      t[i] = x[::-1]
   t = " ".join(t)
   return t


if __name__ == '__main__':
   s = "Let's take LeetCode contest"
   print(s)
   print(reverseWords(s))
