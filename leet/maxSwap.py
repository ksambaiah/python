#!/usr/bin/env python3
'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
'''
def maxnum(i):
    a = 0
    t = i
    a = []
    while t:
      a.append(t % 10)
      print(a)
      t = t // 10
    a = rev(a)
    max = a[0]
    j = 1
    for j in a:
       if a[j] < max:
          max = a[j]


if __name__ ==  '__main__':
    num = 1731
    print(num)
    print(maxnum(num))
