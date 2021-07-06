#!/usr/bin/env python3

'''
Merge Two Sorted Lists
Definition for singly-linked list.
'''

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def __repr__(self):
        return self.val

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = d = ListNode(0)
        while l1 and l2:
           if l1.val < l2.val:
              cur.next = l1
              l1 = l1.next
           else:
              cur.next = l2
              l2 = l2.next
           cur = cur.next
               
        cur = l1 or l2
        return d.next

if __name__ == '__main__':
   a = ListNode("1")
   b = ListNode("2")
   c = ListNode("4")
   a.next = b
   b.next = c
   print(a)
   d = ListNode("1")
   e = ListNode("3")
   d.next = e
   f = ListNode("4")
   e.next = f
   x =  Solution()
   print(x.mergeTwoLists(a, d))
