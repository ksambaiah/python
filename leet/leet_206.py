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
def reverseList(list):
   # initialize variables
   previous = None         # `previous` initially points to None
   current = list.head     # `current` points at the first element
   following = current.next    # `following` points at the second element

   # go till the last element of the list
   while current:
      current.next = previous # reverse the link
      previous = current      # move `previous` one step ahead
      current = following         # move `current` one step ahead
      if following:               # if this was not the last element
          following = following.next    # move `following` one step ahead

   list.head = previous
   return list


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
    print("size is ", llist.size())
    print(reverseList(llist))
 
