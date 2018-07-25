# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getleaves(root1) == self.getleaves(root2)
        
    def getleaves(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
                continue
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
