
"""
Given the root of a binary tree, then value v and depth d, 
you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: 
    given a positive integer depth d, for each NOT null tree nodes N in depth d-1, 
    create two tree nodes with value v as N's left subtree root and right subtree root. 
    And N's original left subtree should be the left subtree of the new left subtree root, 
    its original right subtree should be the right subtree of the new right subtree root. 
    If depth d is 1 that means there is no depth d-1 at all, 
    then create a tree node with value v as the new root of the whole original tree, 
    and the original tree is the new root's left subtree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        queue = [root]
        depth = 1
        if depth == d:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        while depth < d - 1:
            tmp = []
            for node in queue:
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)
            queue = tmp
            depth += 1
        for node in queue:
            if node:
                new_left = TreeNode(v)
                new_right = TreeNode(v)
                new_left.left = node.left
                new_right.right = node.right
                node.left = new_left
                node.right = new_right
        return root
