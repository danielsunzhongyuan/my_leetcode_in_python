"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
#         target, pre = self.searchBST(root, None, key)
#         if not target:
#             return root
#         if not pre:
#             return self.adjustTree(target)
#         if pre.left == target:
#             pre.left = self.adjustTree(target)
#         elif pre.right == target:
#             pre.right = self.adjustTree(target)
#         return root
        
#     def searchBST(self, root, pre, val):
#         if not root:
#             return None, pre
#         if root.val == val:
#             return root, pre
#         if root.val > val:
#             return self.searchBST(root.left, root, val)
#         return self.searchBST(root.right, root, val)
    
#     def adjustTree(self, node):
#         if not node.left:
#             return node.right
#         if not node.right:
#             return node.left
        
#         new_root = node.left
#         cur = new_root
#         while cur.right:
#             cur = cur.right
#         cur.right = node.right
#         return new_root

        if root == None:
            return None
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            
            node = self.nextNode(root)
            root.val = node.val
            root.right = self.deleteNode(root.right , root.val)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left , key)
        else:
            root.right = self.deleteNode(root.right , key)
        return root
        
        
    def nextNode(self, node):
        curr = node.right
        while curr != None and curr.left != None:
            curr = curr.left
        return curr
