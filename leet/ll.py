#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(2)
a.next = a(3)
print(a.val)
print(a.next.val)
