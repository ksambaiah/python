#!/usr/bin/env python3

'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
         if p is None and q is None:
            return True
         if p is not None and q is not None:
            return p.val == q.val and isSame(p.left, q.left) and isSameTree(p.right, q.right)
         return False


def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         if data is not None:
            temp.left = TreeNode(data)
         else:
            temp.left = TreeNode(0)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         if data is not None:
            temp.right = TreeNode(data)
         else:
            temp.right = TreeNode(0)
         break
      else:
         que.append(temp.right)

def make_tree(elements):
   Tree = TreeNode(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree

tree1 = make_tree([2,null,1])
tree2 = make_tree([2,null,1])
ob1 = Solution()
print(ob1.isSameTree(tree1,tree2))
