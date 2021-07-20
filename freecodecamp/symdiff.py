#!/usr/bin/env python3

''' 
Sym difference of two lists. A and B are two lists sym diff is
A- B union B -A
'''

def sym(A, B):
    return list(set(A) - set(B).union(set(B) - set(A)))


if __name__ == '__main__':
   A = [1,2,3,4,6]
   B = [-1.1,5,3,7,9,0]
   print(A,B)
   print(sym(A,B))
