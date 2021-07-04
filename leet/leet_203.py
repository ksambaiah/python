#!/usr/bin/env python3
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return self.data

class LinkedList:
    def __int__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
           nodes.append(node.data)
           node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def size(self):
        node = self.head
        nodes = 0
        while node is not None:
            nodes += 1
            node = node.next
        return nodes

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
           self.head = newNode
        current_node = self.head
        while current_node.next is not None:
           current_node = current_node.next
        current_node.next = newNode
    
def getLastNode(llist):
    clist = llist.head
    while clist.next is not None:
         clist = clist.next
    return clist.data
def removeElements(head: Node, val: int) -> Node:
    dummy = Node(float("-inf"))
    dummy.next = head
    prev, curr = dummy, dummy.next
    while curr:
       if curr.data == val:
          prev.next = curr.next
       else:
          prev = curr
       curr = curr.next
    return dummy.next

if __name__ == '__main__':
    llist = LinkedList()
    a = Node("1")
    llist.head = a
    b = Node("2")
    a.next = b
    c = Node("3")
    b.next = c
    d = Node("4")
    c.next = d 
    e = Node("5")
    d.next = e
    print(llist)
    print(removeElements(a, "4"))
    print(llist)
    print(removeElements(a, "2"))
    print(llist)
 
