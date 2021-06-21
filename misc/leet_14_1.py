#!/usr/bin/env python3

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
def longestCommonPrefix( strs) -> str:
        st = strs[0]
        for i in range(1, len(strs)):
            if st and strs[i]:
                if len(st) <= len(strs[i]):
                    l = len(st)
                else:
                    l = len(strs[i])
                for k in range(l):
                    if st[k] == (strs[i])[k]:
                        k += 1
                    else:
                        break
                st = st[0:k]
            else:
                return ""
        return st


if __name__ == '__main__':
   strs = ["flower","flow","flight", ""]
   print(strs)
   print(longestCommonPrefix(strs))
