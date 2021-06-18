#!/usr/bin/env python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

llist = LinkedList()
first_node = Node("a")
llist.head = first_node
print(llist.head)
print(llist)
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
print(llist)
second_node.next = third_node
print(llist)
print(first_node)
print(second_node)
print(third_node)
