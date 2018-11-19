# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def helper(self, node):
        if node is None:
            return [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        res = [0, 0]
        res[0] = left[1] + right[1] + node.val
        res[1] = max(left[0], left[1]) + max(right[0], right[1])
        return res

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return max(res[0], res[1])
