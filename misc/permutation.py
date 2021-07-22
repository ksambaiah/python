#!/usr/bin/env python3

'''
Permutations of a string
abc
abc, acb, bac, bca, cab, cba
'''
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp

def permutations(ch, curr_index=0):
 
   if curr_index == len(ch) - 1:
       yield (''.join(ch))
 
   for i in range(curr_index, len(ch)):
       swap(ch, curr_index, i)
       permutations(ch, curr_index + 1)
       swap(ch, curr_index, i)
    


if __name__ == '__main__':
    str = "abc"
    print(str)
    perms = permutations(list(str))
    for s in perms:
       print(s)
