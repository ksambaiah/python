#!/usr/bin/env python3
import random
import collections

def constrainedSubsetSum( nums, k) -> int:
    # dp[i] := max sum of non-empty subsequence in nums[0..i]
    dp = [0] * len(nums)
    # q stores dp[i - k], dp[i - k + 1], ..., dp[i - 1] whose values are > 0 in decreasing order
    q = collections.deque()
    for i, num in enumerate(nums):
      if q:
        dp[i] = max(q[0], 0) + num
      else:
        dp[i] = num
      while q and q[-1] < dp[i]:
        q.pop()
      q.append(dp[i])
      if i >= k and dp[i - k] == q[0]:
        r = q.popleft()
    return max(dp)

if __name__ == '__main__':
   arr = []
   k = 2
   for i in range(9):
       arr.append(random.randint(-99999, 99999))
   print(arr)
   sum = constrainedSubsetSum(arr,k) 
   print(sum)
