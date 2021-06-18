#!/usr/bin/env python3

def merge(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
       if a[i] <= b[j]:
          c.append(a[i])
          i = i + 1
       else:
          c.append(b[j])
          j = j + 1
    while i < len(a):
          c.append(a[i])
          i += 1
    while j < len(b):
          c.append(b[j])
          j += 1
    return c
if __name__ == '__main__':
    a = [1, 2, 3, 4, 10, 15, 19, 20, 21]
    b = [0, 3, 10, 22, 23, 24, 25,100,900]
    print(a)
    print(b)
    c = merge(a,b)
    print(c)
