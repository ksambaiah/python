#!/usr/bin/env python3

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
def strmatch(a, b):
    if len(a) <= len(b):
       l = len(a)
    else:
       l = len(b)
    for i in range(l):
        if a[i] == b[i]:
            i += 1
        else:
            return a[0:i]
    return a[0:i]

def Longsubseq(stSeq):
    st = stSeq[0]
    for i in range(1, len(stSeq)): 
        if st:
            st = strmatch(st,stSeq[i])
        else:
            return ""
    return st

if __name__ == '__main__':
   strs = ["flower","flow","flight", "lll"]
   print(strs)
   print(Longsubseq(strs))
