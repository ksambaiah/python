#!/usr/bin/env python3


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__( x):
#         self.val = x
#         self.next = None

def reverseList(head):
     return reverse(head)

def reverse(node, prev=None):
     if not node:
         return prev
     n = node.next
     node.next = prev

     return reverse(n, node)

if __name__ == '__main__':
     a = reverseList([1,2,8,-90,-2,-1,0])
     print(a)
