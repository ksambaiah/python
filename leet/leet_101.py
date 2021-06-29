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
    def isSymmetric(self, root):
         if root is None:
            return True
         return self.isSymmetricRecu(root.left, root.right)
    def isSymmetricRecu(self, left, right):
         if left is None and right is None:
              return True
         if left is None or right is None or left.val != right.val:
               return False
         return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)

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

tree1 = make_tree([1,2,2,3,4,4,3])
#tree1 = make_tree([1,2,9,3,4,4,3])
ob1 = Solution()
print(ob1.isSymmetric(tree1))
