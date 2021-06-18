#!/usr/bin/env python3
'''
Sample program to write linked list

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
    

if __name__ == '__main__':
    llist = LinkedList()
    a = Node("1")
    llist.head = a
    print(llist)
    b = Node("2")
    a.next = b
    c = Node("3")
    b.next = c
    print(llist)
    print(llist.size())
    llist.append("abcd")
    print(llist)
