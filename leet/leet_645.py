#!/usr/bin/env python3
'''

'''

def findErrorNums(nums):
    dict = {}
    arr = []
    sum1 = 0
    for i in nums:
        if i not in dict.keys():
            sum1 += i
            dict[i] = 1
        else:
            arr.append(i)
    size = len(dict.keys()) + 1
    sum = int(( size * (size+1)) / 2)
    arr.append(sum-sum1)
    return arr
if __name__ == '__main__':
    arr = [1,2,3,3,5]
    print(arr)
    print(findErrorNums(arr))
