#!/usr/bin/env python3

'''
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
'''

def matchWords( wordsDict, word1: str, word2: str) -> int:
    temp = wordsDict
    a = []
    while temp:
       i = temp.index(word1)
       a.append(i)
       temp = temp[i+1:]
    if word1 != word2:
       b = []
       temp = wordsDict
       while temp:
          i = temp.index(word1)
          a.append(i)
          temp = temp[i+1:]
5 7 8 9
3 10 12
   
if __name__ ==  '__main__':

   wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
   word1 = "makes"
   word2 = "makes"
   print(matchWords(wordsDict, word1, word2))
