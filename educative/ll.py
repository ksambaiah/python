#!/usr/bin/env python3

'''
Linked list and Node implementation in Python3
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        n = Node(data)
        if self.head is None:
           self = n
           return
        lastNode = self.head
        while lastNode.next is not None:
           lastNode = lastNode.next
        lastNode.next = n

    def prepend(self, data):
        n = Node(data)
        n.next = self.head
        self.head  = n
   
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("prev_node doesn't exist, quitting")
        n = Node(data)
        n.next = prev_node.next
        prev_node.next = n     
 
    def delete_key(self, key):
        curr_node = self.head
        d = self.head
        if curr_node and curr_node.data == key:
            curr_node = curr_node.next
            self.head = curr_node
            return
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None

    def delete_pos(self, pos):
        curr_node = self.head
        if pos == 0:
            curr_node = curr_node.next
            return 
        prev_node = None
        while pos > 0:
            prev_node = curr_node
            curr_node = curr_node.next
            pos  -= 1
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        curr_node = None
    def __repr__(self):
        tmp  = self.head
        mem = []
        while tmp is not None: 
           mem.append(tmp.data)
           tmp = tmp.next
        return " -> ".join(mem) 

    def length(self):
       tmp = self.head
       n = 0
       while tmp is not None:
           tmp = tmp.next
           n += 1
       return n

if __name__ == "__main__":
    a = Node("5")
    print(a)
    b = Node("6")
    a.next = b
    s = LinkedList()
    s.head = a
    c = Node("7")
    b.next = c
    print(s)
    s.append("100")
    print(s)
    s.append("101")
    s.prepend("-100")
    print(s)
    s.insert_after_node(c, "2000")
    print(s)
    print(s.length())
    s.delete_key("-100")
    print(s)
    s.delete_key("100")
    print(s)
    s.delete_key("2000")
    print(s)
    s.delete_pos(2)
    print(s)
    print(s.length())
