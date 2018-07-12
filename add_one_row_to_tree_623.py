# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
