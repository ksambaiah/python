#!/usr/bin/env python3
''' leetcode 12268 '''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    sumll = ListNode
    followup = 0
    while l1.next or l2.next:
        if l1.next and l2.next:
            sumll.val = ( l1.next + l2.next + followup ) % 10
            followup = int (( l1.next + l2.next + followup ) // 10)
        elif l1.next:
            sumll.val = ( l1.next  + followup ) % 10
            followup = int (( l1.next  + followup ) // 10)
        elif l2.next:
            sumll.val = ( l2.next  + followup ) % 10
            followup = int (( l2.next  + followup ) // 10)
    if followup:
        sumll.val = followup
    return sumll

if __name__ == '__main__':
   a = ListNode
   a.append(2)
   a.append(9)
   a.append(4)
   b.val = 5
   b.next.val = 6
   b.next.next.val = 4
   r = addTwoNumbers(a, b)
   print(r.val, r.next.val, r.next.next.val)
