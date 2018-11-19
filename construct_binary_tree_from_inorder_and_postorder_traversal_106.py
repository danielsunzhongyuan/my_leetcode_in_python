"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        length = len(inorder)
        if length == 0:
            return
        return self.buildTreeRecursion(inorder, postorder, 0, length - 1, 0, length - 1)

    def buildTreeRecursion(self, inorder, postorder, lIn, rIn, lPost, rPost):
        if lPost > rPost:
            return None
        middle_node = TreeNode(postorder[rPost])
        if lPost == rPost:
            return middle_node
        m = rIn
        while m >= lIn and inorder[m] != postorder[rPost]:
            m -= 1

        middle_node.left = self.buildTreeRecursion(inorder, postorder, lIn, m - 1, lPost, rPost - (rIn - m) - 1)
        middle_node.right = self.buildTreeRecursion(inorder, postorder, m + 1, rIn, rPost - (rIn - m), rPost - 1)
        return middle_node
