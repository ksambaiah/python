#!/usr/bin/env python3
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''
def Permu(a):
    for i in range(len(a)-2, 1, -1):
        if a[-1] > a[i]:
           temp = a[i]
           a[i] = a[-1]
           a[-1] = temp
           return a
    return a[::-1]


if __name__ == '__main__':
    a = [100,103,109,101]
    print(a)
    b = Permu(a)
    print(b)
